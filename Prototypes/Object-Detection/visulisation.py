import cv2 
import argparse
import json
import numpy as np
from ultralytics import YOLO   
import supervision as sv 

#Please make sure that supervision is verison==0.2.1 or it will crash 
###From  https://www.youtube.com/watch?v=QV85eYOb7gk&t=633s #######

def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="YOLOv8 live")
    parser.add_argument(
        "--webcam-resolution",
        default=[1280,720],
        nargs=2,
        type=int
    )
    args = parser.parse_args()
    return args


def GetJson(file_name):
    with open(file_name, "r") as json_file:
        # Load the JSON data from the file
        data = json.load(json_file)

    receipts = data.get("receipts", [])
    return receipts

def GetCurrentStep(receipt, model,Step):
    CurrentStep = [
        receipt[Step]["Human"],
        *receipt[Step]["AI"].split(":") 
    ]
    #Change the currentstep for AI to the number index on the model
    CurrentStep[1] = {i for i in model.model.names if model.model.names[i]==CurrentStep[1]}
    if(len(CurrentStep[1]) == 0):
        CurrentStep[1] = -1
    else:
        CurrentStep[1] = list(CurrentStep[1])[0]
    CurrentStep[2] = {i for i in model.model.names if model.model.names[i]==CurrentStep[2]}
    if(len(CurrentStep[2]) == 0):
        CurrentStep[2] = -1
    else:
        CurrentStep[2] = list(CurrentStep[2])[0]

    return CurrentStep



def main():
    #Get the receipts from Json file 
    receipts = GetJson("C:/Uni work/Operation Custard/Repo/comp6000-chop-chop/Prototypes/Object-Detection/recipts.json")
    #only get the pancake part of the receipt json file
    pancakeReceipt = receipts[0]["pancake"]
    #Set the current step to be at the start
    args = parse_arguments()
    frame_width,frame_height = args.webcam_resolution

    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, frame_width)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, frame_height)

####### Change to the trained data ################
    model = YOLO("C:/Uni work/Operation Custard/Repo/comp6000-chop-chop/Prototypes/Object-Detection/best.pt")
    index = 0
    CurrentStep = GetCurrentStep(pancakeReceipt,model,index)


    # Create a blank image (you can also load an existing image)
    width, height = 800, 600
    image = np.zeros((height, width, 3), dtype=np.uint8)  # Create a black image


# Set the position and other properties for the text
    position = (100, 200)  # (x, y) coordinates/
    font_scale = 1
    font_color = (255, 255, 255)  # White color in BGR
    font_thickness = 2
    font_face = cv2.FONT_HERSHEY_SIMPLEX


    while True:
        ret, frame = cap.read()
        result = model(frame)[0] 
        detections = sv.Detections.from_yolov8(result)

        image = np.zeros((height, width, 3), dtype=np.uint8)  # Create a black image

        cv2.putText(image, CurrentStep[0], position, font_face, font_scale, font_color, font_thickness)

        #looking at all objects that are being detecteqd, if cut onion but no whole onion then send a response to API call
        print(CurrentStep[2])
        print(detections.class_id)
        if CurrentStep[2] in detections.class_id:
            print("Found")
            if not (CurrentStep[1] in detections.class_id):
                print("All done chopping ready to move on")
                #For now it just ends the program but will need to send a response to the API
                CurrentStep = GetCurrentStep(pancakeReceipt,model,index)
                index = index + 1
            else:
                print("Chopping is going on at the moment")
        elif CurrentStep[1] in detections.class_id:
            print("Found onion no chopping has started!")
        cv2.imshow("Image with Text", image)
        if(cv2.waitKey(30) == 27):
            break
if __name__ == "__main__":
    main()
import cv2 
import argparse
import json
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


def main():
    args = parse_arguments()
    frame_width,frame_height = args.webcam_resolution

    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, frame_width)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, frame_height)

####### Change to the trained data ################
    model = YOLO("C:/Uni work/Operation Custard/Repo/comp6000-chop-chop/Prototypes/Object-Detection/best.pt")


    while True:
        ret, frame = cap.read()
        result = model(frame)[0] 
        detections = sv.Detections.from_yolov8(result)

        #looking at all objects that are being detected, if cut onion but no whole onion then send a response to API call
        if 0 in detections.class_id:
            if not (1 in detections.class_id):
                print("All done chopping ready to move on")
                #For now it just ends the program but will need to send a response to the API
                exit()
            else:
                print("Chopping is going on at the moment")
        elif 1 in detections.class_id:
            print("Found onion no chopping has started!")
        
        if(cv2.waitKey(30) == 27):
            break
if __name__ == "__main__":
    main()
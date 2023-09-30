import cv2
import argparse
import json
import numpy as np
from ultralytics import YOLO
import supervision as sv

#Please make sure that the Supervision verision is on 0.2.1 to do this, *pip unistall supervision , pip install supervision==0.2.1

#Display class is for all the setting and displaying cv2 window with text
class Display:
    def __init__(self, resolution):
        self.frame_width, self.frame_height = resolution
        self.cap = cv2.VideoCapture(0)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, self.frame_width)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, self.frame_height)
        self.font_scale = 1
        self.font_color = (255, 255, 255)
        self.font_thickness = 2
        self.font_face = cv2.FONT_HERSHEY_SIMPLEX
        self.image = np.zeros((self.frame_height, self.frame_width, 3), dtype=np.uint8)

    def set_text(self, text):
        position = (100, 200)
        self.image = np.zeros((self.frame_height, self.frame_width, 3), dtype=np.uint8)
        cv2.putText(self.image, text, position, self.font_face, self.font_scale, self.font_color, self.font_thickness)

    def show_image(self):
        cv2.imshow("Image with Text", self.image)

    def release(self):
        self.cap.release()
        cv2.destroyAllWindows()





#Does all the AI detection and also the Json reading
class DetectionAI:

    def __init__(self, model_location, json_location,Recipt):
        self.model = YOLO(model_location)
        self.index_Class = {idx: name for idx, name in enumerate(self.model.model.names)}
        self.receipt = self.get_json(json_location)[0][Recipt]
        self.index = 0
        self.current_step = self.get_current_step()

    def get_json(self, file_name):
        with open(file_name, "r") as json_file:
            data = json.load(json_file)
        return data.get("receipts", [])

    def get_current_step(self):
        ReciptStepsForAI = self.receipt[self.index]["AI"][0]
        BgDetects = ReciptStepsForAI["BgDetects"][0]
        IngredentIndex = next((i for i in self.model.model.names if self.model.model.names[i] == ReciptStepsForAI["Ingredent"]), None)
        DetectsIndex =  next((i for i in self.model.model.names if self.model.model.names[i] == ReciptStepsForAI["Detects"]), None)


        return [self.receipt[self.index]["Human"],IngredentIndex,DetectsIndex]

#Add the detection to each frame
    def process_frame(self, frame):
        result = self.model(frame)[0]
        detections = sv.Detections.from_yolov8(result)
        return detections

#Update to what the next recipt step should be
    def update_step(self):
        self.index += 1
        self.current_step = self.get_current_step()


#Passing in all the arguments you might want to change
def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="YOLOv8 live")
    parser.add_argument("--resolution", default=[1280, 720], nargs=2, type=int)
    parser.add_argument("-m", "--model", default= "C:/Uni work/Operation Custard/Repo/comp6000-chop-chop/Prototypes/Object-Detection/best.pt",required=False, help="Path to the model location")
    parser.add_argument("-j", "--json", default= "C:/Uni work/Operation Custard/Repo/comp6000-chop-chop/Prototypes/Object-Detection/recipts.json",required=False, help="Path to the JSON location")
    parser.add_argument("-r", "--Recipt", default="pancake", help="What recipt you want to use")
    return parser.parse_args()

def main():
    args = parse_arguments()
    #init both display class and detectionAI
    display = Display(args.resolution)
    ai = DetectionAI(args.model, args.json,args.Recipt)

    #Big while loop for all the logic that happens each frame
    while True:
        ret, frame = display.cap.read()
        detections = ai.process_frame(frame)
        display.set_text(ai.current_step[0])
        display.show_image()
        #Check to see if only the detects id is in the detections and the Ingredent isn't
        if ai.current_step[2] in detections.class_id:
            if not (ai.current_step[1] in detections.class_id):
                ai.update_step()
        #Add a timer that checks if we need to str

        #Add a timer to check if there is any boil over 

        if cv2.waitKey(30) == 27:
            break

    display.release()

if __name__ == "__main__":
    main()

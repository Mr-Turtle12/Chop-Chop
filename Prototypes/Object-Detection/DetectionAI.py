import json
from ultralytics import YOLO
import supervision as sv


#Does all the AI detection and also the Json reading
class DetectionAI:

    def __init__(self, model_location, json_location,receipt):
        self.model = YOLO(model_location)
        self.index_Class = {idx: name for idx, name in enumerate(self.model.model.names)}
        self.receipt = self.get_json(json_location)[receipt]
        self.index = 0
        self.current_step = self.get_current_step()

    def get_json(self, file_name):
        with open(file_name, "r") as json_file:
            data = json.load(json_file)
        return data.get("Recipt", [])

    def get_current_step(self):
        ReciptStepsForAI = self.receipt[self.index]["AI"]
        IngredentIndex = next((i for i in self.model.model.names if self.model.model.names[i] == ReciptStepsForAI["Ingredent"]), None)
        DetectsIndex =  next((i for i in self.model.model.names if self.model.model.names[i] == ReciptStepsForAI["Detects"]), None)

        return [self.receipt[self.index]["Human"],IngredentIndex,DetectsIndex]

#Add the detection to each frame
    def process_frame(self, frame):
        result = self.model(frame)[0]
        detections = sv.Detections.from_yolov8(result)
        if self.current_step[2] in detections.class_id:
            if not (self.current_step[1] in detections.class_id):
                self.update_step()

#Update to what the next receipt step should be
    def update_step(self):
        self.index += 1
        self.current_step = self.get_current_step()
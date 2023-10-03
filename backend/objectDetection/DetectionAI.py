from ultralytics import YOLO
import supervision as sv


#Does all the AI detection
class DetectionAI:
    def __init__(self, modelLocation):
        #Set the confidence_threshold to 0.6
        self.model = YOLO(modelLocation, conf=0.6)
        self.index_Class = {idx: name for idx, name in enumerate(self.model.model.names)}

    #Check if an object is in the item 
    def find_object(self,item,detections):
        item_index = next((i for i in self.model.model.names if self.model.model.names[i] == item), None)
        if item_index in detections.class_id:
            return True
        else:
            return False
        
    #This function will return true of false for each item that is passed into the object
    def process_frame(self, frame,items):
        result = self.model(frame)[0]
        detections = sv.Detections.from_yolov8(result)
        if isinstance(items, str):
            return [self.find_object(items,detections)]
        else:
            found = []
            for item in items:
                found.append(self.find_object(object,detections))
            return found
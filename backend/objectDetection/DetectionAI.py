from ultralytics import YOLO
import supervision as sv


#Does all the AI detection
class detectionAI:
    def __init__(self, modelLocation):
        self.model = YOLO(modelLocation)
        self.index_Class = {idx: name for idx, name in enumerate(self.model.model.names)}

    #Check if an object is in the item 
    def findObject(self,item,detections):
        itemIndex = next((i for i in self.model.model.names if self.model.model.names[i] == item), None)
        if itemIndex in detections.class_id:
            return True
        else:
            return False
        
    #This function will return true of false for each item that is passed into the object
    def processFrame(self, frame,items):
        result = self.model(frame)[0]
        detections = sv.Detections.from_yolov8(result)
        if isinstance(items, str):
            return self.findObject(items,detections)
        else:
            found = []
            for item in items:
                found.append(self.findObject(object,detections))
            return found
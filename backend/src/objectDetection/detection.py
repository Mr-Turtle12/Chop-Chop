from ultralytics import YOLO
import supervision as sv

# GLOBAL VAR
CONFIDENCE_THRESHOLD = float(0.4)


#This class is used for processing the frame and adding the detections from the AI to the frame
class Detection:
    def __init__(self, modelLocation):
        self.model = YOLO(modelLocation)
        self.index_Class = {
            idx: name for idx, name in enumerate(self.model.model.names)
        }

    # Check if an object is in the item
    def find_item(self, item, detections):
        item_index = next(
            (i for i in self.model.model.names if self.model.model.names[i] == item),
            None,
        )
        return item_index in detections.class_id

    # take care if the items var is an item or array of items you want to check

    def check_items(self, items, detections):
        if isinstance(items, str):
            return [self.find_item(items, detections)]
        else:
            found = []
            for item in items:
                found.append(self.find_item(item, detections))
            return found

    # This function will return true of false for each item that is passed into the object

    def process_frame(self, frame, items):
        global CONFIDENCE_THRESHOLD
        result = self.model(frame)[0]
        detections = sv.Detections.from_yolov8(result)
        # Set detection to only detect on confidence threshold
        detections = detections[detections.confidence > CONFIDENCE_THRESHOLD]
        return self.check_items(items, detections)

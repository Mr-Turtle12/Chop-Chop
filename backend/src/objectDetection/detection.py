from ultralytics import YOLO
import supervision as sv


# This class is used for processing the frame and adding the detections from the AI to the frame
class Detection:
    def __init__(self, model_location, confidence_threshold):
        self.model = YOLO(model_location)
        self.confidence_threshold = confidence_threshold

    # This function will return true of false for each item that is passed into the object
    def get_tags_from_class_ids(self, class_ids):
        tags = []
        for class_id in class_ids:
            tag = self.model.names.get(class_id, "unknown")
            tags.append(tag)
        return tags

    def process_frame(self, frame, progression_object,inhibitor):
        result = self.model(frame)[0]
        detections = sv.Detections.from_yolov8(result)
        # Set detection to only detect on confidence threshold
        detections = detections[detections.confidence > self.confidence_threshold]
        class_names = self.get_tags_from_class_ids(detections.class_id)
        return progression_object in class_names and inhibitor not in class_names


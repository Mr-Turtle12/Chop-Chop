from ultralytics import YOLO
import supervision as sv
from backend.src.utils.utils import log


class Detection:
    def __init__(self, model_location, confidence_threshold):
        """Initializes the Detection class.
        Args:
            model_location (str): The location of the YOLO model.
            confidence_threshold (float): The confidence threshold for detections.
        """
        self.model = YOLO(model_location)
        self.last_tag = ["Start"]
        self.confidence_threshold = confidence_threshold

    def get_tags_from_class_ids(self, class_ids):
        """Retrieves tags from the provided class IDs.
        Args:
            class_ids (list): A list of class IDs.
        Returns:
            list: A list of tags corresponding to the class IDs.
        """
        tags = []
        for class_id in class_ids:
            tag = self.model.names.get(class_id, "unknown")
            tags.append(tag)
        return tags

    def process_frame(self, frame, progression_object, inhibitor):
        """Processes the frame for object detection.
        Args:
            frame (str): The frame to process.
            progression_object (str): The object to detect for progression.
            inhibitor (str): The object to detect as an inhibitor.
        Returns:
            bool: True if the progression object is in the detected class names and the inhibitor is not, otherwise False.
        """
        result = self.model(frame, verbose=False)[0]
        detections = sv.Detections.from_yolov8(result)
        detections = detections[detections.confidence > self.confidence_threshold]
        class_names = self.get_tags_from_class_ids(detections.class_id)
        if self.last_tag != class_names:
            log(class_names, "Detect")
        self.last_tag = class_names
        return progression_object in class_names and inhibitor not in class_names

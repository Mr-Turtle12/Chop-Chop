import pytest
import cv2
from unittest.mock import MagicMock
import sys
sys.path.append('./backend/src')
import objectDetection 

class MockCamera:
    def __init__(self,image):
        self.cap = MagicMock()
        self.image = image
    
    def read(self):
        frame = cv2.imread(self.image)
        return frame

    def show(self, frame):
        pass
    
    def release(self):
        pass

@pytest.fixture
def detector():
    detector = objectDetection.ObjectDetection("./Trained-Data/Version3/runs/detect/train/weights/best.pt", 0)
    return detector
    
# Test one photo 
# Test One correct:
def test_one_correct(detector):
    detector.cameraObj = MockCamera( "./backend/tests/objectDetectionTest/photos/hasRed-Onion.jpg")
    result = detector.check_items("Red-Onion")
    assert result == [True]

# Test one fail:
def test_one_fail(detector):
    detector.cameraObj = MockCamera("./backend/tests/objectDetectionTest/photos/hasRed-Onion.jpg")
    result = detector.check_items("Chopped-Red-Onion")
    assert result == [False]

# Test one correct, one fail:
def test_one_correct(detector):
    detector.cameraObj = MockCamera("./backend/tests/objectDetectionTest/photos/hasRed-Onion.jpg")
    result = detector.check_items(["Chopped-Red-Onion", "Red-Onion"])
    assert result == [False,True]

# Test two fail:
def test_one_correct(detector):
    detector.cameraObj = MockCamera("./backend/tests/objectDetection/photos/hasRed-Onion.jpg")
    result = detector.check_items(["Chopped-Red-Onion", "Carrot"])
    assert result == [False,False]


# Assuming you have a test image named 'test_image.jpg' in the same directory

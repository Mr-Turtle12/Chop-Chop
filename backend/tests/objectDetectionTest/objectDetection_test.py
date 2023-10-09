import pytest
from unittest.mock import Mock, patch
import sys
sys.path.append('./backend/src')
import objectDetection

# Use pytest -q ".\backend\tests\objectDetectionTest\objectDetection_test.py" to run the test; should return 5 passed.
def CallObject():
    return objectDetection.ObjectDetection("./Trained-Data/Version3/runs/detect/train/weights/best.pt", "./backend/tests/objectDetectionTest/photos/hasRed-Onion.jpg")

# This test will check if you pass one item into the check_items function that is in the photo; should return true.
def test_single_true():
    detObj = CallObject()
    detection = detObj.check_items("Red-Onion")
    assert detection == [True]

# This test will check if you pass one item into the check_items function that is not in the photo; should return false.
def test_single_false():
    detObj = CallObject()
    detection = detObj.check_items("Chopped-Red-Onion")
    assert detection == [False]

# This test will check if you pass more than one item into the check_items function where one is in the photo and one isn't in the photo; should return [True,False].
def test_multiple_true_false():
    detObj = CallObject()
    detection = detObj.check_items(["Red-Onion","Chopped-Red-Onion"])
    print(detection)
    assert detection == [True,False]

# This test will check if you pass more than one item into the check_items function where both aren't in the photo; should return [False,False].
def test_multiple_falses():
    detObj = CallObject()
    detection = detObj.check_items(["Carrot","Chopped-Red-Onion"])
    assert detection == [False,False]

# This test will check if you pass more than one item into the check_items function where both are in the photo; should return [True,True].
def test_multiple_trues():
    detObj = CallObject()
    detection = detObj.check_items(["Red-Onion","White-Onion"])
    assert detection == [True,True]

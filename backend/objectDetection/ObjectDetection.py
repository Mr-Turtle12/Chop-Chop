
# How to call:
# Initialize the object:
# objDet = ObjectDetection.ObjectDetection("./Database/best.pt", 0)

# To check for a food item, e.g., "onion":
# objDet.CheckItems("onion")
# return:
# [False]

# To check for more than one food item, e.g., "onion" and "carrot":
# objDet.CheckItems(["onion", "carrot"])
# return:
# [False,False]

# Once all detecting have finished:
# objDet.End()



import DetectionAI
import GetCamare


class ObjectDetection:
    def __init__(self, model,camareID):
        self.AI = DetectionAI.detectionAI(model)
        self.camare = GetCamare.getCamare([1280, 720],camareID)
    
#Will set everything up to check the frame for any objects that is passed in to it
    def CheckItems(self, objects):
        _, frame = self.camare.cap.read()
        #This will return an array of True and  False
        return self.AI.process_frame(frame,objects)
    
    #To be called at the end
    def end(self):
        self.camare.release()
    
    

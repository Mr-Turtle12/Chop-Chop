import argparse
import Display
import DetectionAI

#Please make sure that the Supervision verision is on 0.2.1 to do this, *pip unistall supervision , pip install supervision==0.2.1
#Passing in all the arguments you might want to change
def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="YOLOv8 live")
    parser.add_argument("--resolution", default=[1280, 720], nargs=2, type=int)
    parser.add_argument("-m", "--model", default= "./Trained-Data/Version3/runs/detect/train/weights/best.pt",required=False, help="Path to the model location")
    parser.add_argument("-j", "--json", default= "./Prototypes/Object-Detection/recipts.json",required=False, help="Path to the JSON location")
    parser.add_argument("-r", "--receipt", default="pancake", help="What receipt you want to use")
    return parser.parse_args()

def main():
    args = parse_arguments()
    #init both display class and detectionAI
    display = Display.Display(args.resolution)
    ai = DetectionAI.DetectionAI(args.model, args.json,args.receipt)

    #Big while loop for all the logic that happens each frame
    while True:
        ret, frame = display.cap.read()
        #Check to see if anything has been detected
        ai.process_frame(frame)
        ##Set the Text to the current  step
        display.set_text(ai.current_step[0])
        #Show iamge
        display.show_image()
        #Break out of loop if pressed esc
        if display.Breakloop():
            break

    display.release()

if __name__ == "__main__":
    main()

# You have 3 args that you can change --model (location of the model), --json (location of the json file) and --receipt (What receipt, make sure that the receipt is in the json file)

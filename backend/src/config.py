from datetime import datetime
import os

# Logging:
timestamp = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
API_LOG_PATH = f"logs/API_logs_{timestamp}.log"
DETECT_LOG_PATH = f"logs/Detect_logs_{timestamp}.log"
# AI Settings
MODEL_LOCATION = "../../Trained-Data/Version4/runs/detect/train/weights/best.pt"
CONFIDENCE_THRESHOLD = float(0.6)
# Interpreter
DETECT_FRAMES = 10
DETECT_THRESHOLD = 7
# Camera settings
CAMERA_IDS = [0, 1]
# API settings
WEBSOCKET_UPDATE_INTERVAL = 1
# Database location
DATABASE = "../../database"
# localhost IP
SERVER_IP = "localhost"

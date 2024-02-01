#!/bin/bash

ServerIP="${1:-localhost}"
PYTHONPATH="$PWD:$PYTHONPATH"

replace_config() {
    ConfigServerIP=$1
    configFilePath="backend/src/config.py"
    configContent=$(<"$configFilePath")

    configContent=$(echo "$configContent" | sed "s/SERVER_IP = \".*\"/SERVER_IP = \"$ConfigServerIP\"/")

    root="${PWD//\\//}"
    ModelLocation="$root/Trained-Data/Version4/runs/detect/train/weights/best.pt"
    DatabaseLocation="$root/database"

    configContent=$(echo "$configContent" | sed "s|MODEL_LOCATION = \".*\"|MODEL_LOCATION = \"$ModelLocation\"|")
    configContent=$(echo "$configContent" | sed "s|DATABASE = \".*\"|DATABASE = \"$DatabaseLocation\"|")

    echo "$configContent" > "$configFilePath"
}

replace_store() {
    StoreServerIP=$1
    WebsocketUrl="ws://$StoreServerIP:8765"
    storeFilePath="frontend/src/store/index.js"
    storeContent=$(<"$storeFilePath")
    storeContent=$(echo "$storeContent" | sed "s/websocketUrl: 'ws:\/\/.*/websocketUrl: '$WebsocketUrl',/")

    echo "$storeContent" > "$storeFilePath"
}

replace_config "$ServerIP"
replace_store "$ServerIP"

# Navigate to backend directory and run Python scripts
cd backend/src || exit
python main.py &
python photos.py &
cd ../../frontend || exit
npm run electron:serve &

param(
    [string]$ServerIP = "localhost"
)

$env:PYTHONPATH = "$PSScriptRoot;$env:PYTHONPATH"

function replace_config {
    param (
        $ConfigServerIP
    )

    $configFilePath = "backend/src/config.py"
    $configContent = Get-Content $configFilePath -Raw

    $configContent = $configContent -replace 'SERVER_IP = ".*"', "SERVER_IP = `"$ConfigServerIP`""

    $root = $PSScriptRoot.Replace('\', '/')
    $ModelLocation = "$root/Trained-Data/Version4/runs/detect/train/weights/best.pt"
    $DatabaseLocation = "$root/database"

    $configContent = $configContent -replace 'MODEL_LOCATION = ".*"', "MODEL_LOCATION = `"$ModelLocation`""
    $configContent = $configContent -replace 'DATABASE = ".*"', "DATABASE = `"$DatabaseLocation`""

    $configContent | Set-Content $configFilePath
}

function replace_store {
    param (
        $StoreServerIP 
    )
    $WebsocketUrl = "ws://"+ $StoreServerIP+":8765"
    $storeFilePath = "frontend/src/store/index.js"
    $storeContent = Get-Content $storeFilePath -Raw
    $storeContent = $storeContent -replace "websocketUrl: 'ws://.*", "websocketUrl: `'$WebsocketUrl`',"
    $storeContent | Set-Content $storeFilePath
}

# Call functions after they are defined
replace_config -ConfigServerIP $ServerIP
replace_store -StoreServerIP $ServerIP

# Navigate to backend directory and run Python scripts
cd "backend/src"
Start-Process python -ArgumentList "main.py" -NoNewWindow
Start-Process python -ArgumentList "photos.py" -NoNewWindow

# Navigate to frontend directory and start npm run electron:serve
cd "../../frontend"
Start-Process npm -ArgumentList "run", "electron:serve" -NoNewWindow
cd "..\.."

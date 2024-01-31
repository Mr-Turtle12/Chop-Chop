$env:PYTHONPATH = "$PSScriptRoot;$env:PYTHONPATH"

# Navigate to the backend directory and run the python scripts
cd "backend\src"
# Start main.py
Start-Process python -ArgumentList "main.py" -NoNewWindow

# Start photos.py
Start-Process python -ArgumentList "photos.py" -NoNewWindow

# Navigate to the frontend directory and start npm run electron:serve
cd "..\..\frontend"
Start-Process npm -ArgumentList "run electron:serve" -NoNewWindow

cd "..\"


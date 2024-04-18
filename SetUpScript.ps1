# Install python
Write-Host "Installing Python..."
winget install -e --id Python.Python.3.11
$profile
$env:path="$env:Path;C:\Program Files\Python311"

# Install Python module dependencies from requirements.txt
Write-Host "Installing Python module dependencies..."
py -m pip install -r "backend\requirements.txt"

cd "frontend"
Write-Host "Installing node.js ...."
winget install nodejs
#restarting the env so that you can call npm
$env:Path=(
    [System.Environment]::GetEnvironmentVariable("Path","Machine"),
    [System.Environment]::GetEnvironmentVariable("Path","User")
) -match '.' -join ';'

Write-Host "Installing npm packages..."
npm install
npm install include-media --save-dev
cd ..
if(-not (Test-Path "backend\src\logs\")){
    New-Item -ItemType Directory -Path "backend\src\logs" > $null
}
Write-Host "completed please run WindowsStartUp.ps1 next"
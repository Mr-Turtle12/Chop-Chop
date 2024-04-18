# Check if Python is installed
if (-not (Get-Command python -ErrorAction SilentlyContinue)) {
    Write-Host "Python is not installed. Installing Python..."
    # Download and install Python
    Invoke-WebRequest "https://www.python.org/ftp/python/3.11.5/python-3.11.5-amd64.exe" -OutFile "python-3.11.5-amd64.exe"
    Start-Process -FilePath ".\python-3.11.5-amd64.exe" -ArgumentList "/quiet", "InstallAllUsers=1", "PrependPath=1" -Wait
    Remove-Item -Path "python-3.11.5-amd64.exe"
}else{
    Write-Host "Skipping downloading python as already installed..."
}

# Check if pip is installed
if (-not (Get-Command pip -ErrorAction SilentlyContinue)) {
    Write-Host "Pip is not installed. Installing pip..."
    # Download and install pip
    Invoke-WebRequest "https://bootstrap.pypa.io/get-pip.py" -OutFile "get-pip.py"
    & "python" ".\get-pip.py"
    Remove-Item -Path "get-pip.py"
}else{
    Write-Host "Skipping downloading pip as already installed..."
}


# Install Python module dependencies from requirements.txt
Write-Host "Installing Python module dependencies..."
& "pip" install -r "backend\requirements.txt"


# chagne to frontend dir 
cd "frontend"
if (-not (Get-Command node -ErrorAction SilentlyContinue)){
    Write-Host "Node.js is not installed. Installing node.js ...."
    Invoke-WebRequest "https://nodejs.org/dist/v21.7.3/node-v21.7.3-x64.msi" -OutFile "node-v21.7.3-x64.msi"
    Start-Process -FilePath ".\node-v21.7.3-x64.msi" -ArgumentList "/quiet", "InstallAllUsers=1", "PrependPath=1" -Wait
    Remove-Item -Path "node-v21.7.3-x64.msi"
}else{
    Write-Host "Skipping downloading Node.js as already installed..."
}

# Install npm package include-media
Write-Host "Installing npm packages"
if(-not (Get-Command npm -ErrorAction SilentlyContinue)){
    Write-Host "npm is not installed. Installing npm...."
}else{
    Write-Host "Skipping downloading npm as already installed..."
}
Write-Host "Installing npm packages..."
npm install
npm install include-media --save-dev

Write-Host "completed please run WindowsStartUp.ps1"

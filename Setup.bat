@echo off
echo Installing Python...
winget install --id Python.Python -e --accept-package-agreements --accept-source-agreements
py -m pip install --upgrade pip
py -m pip install pygame-ce
echo Success! Python and pygame-ce have been installed successfully.
pause
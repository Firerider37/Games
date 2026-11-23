@echo off
echo Installing Python...
winget install --id Python.Python -e --accept-package-agreements --accept-source-agreements
py -m pip install --upgrade pip
py -m pip install pygame-ce
py -m pip install questionary
echo Success! Python, pygame-ce and questionary have been installed successfully.
pause
@echo off
REM Activation script for Blockgame virtual environment (Windows)

if not exist ".venv" (
    echo Virtual environment not found. Creating it...
    python setup_venv.py
)

echo Activating virtual environment...
call .venv\Scripts\activate.bat

echo Virtual environment activated!
echo You can now run: python main.py
echo To deactivate later, run: deactivate
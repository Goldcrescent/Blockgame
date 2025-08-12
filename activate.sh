#!/bin/bash
# Activation script for Blockgame virtual environment

if [ ! -d ".venv" ]; then
    echo "Virtual environment not found. Creating it..."
    python setup_venv.py
fi

echo "Activating virtual environment..."
source .venv/bin/activate

echo "Virtual environment activated!"
echo "You can now run: python main.py"
echo "To deactivate later, run: deactivate"
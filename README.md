# Blockgame
A block type game like minecraft, but not exactly (Kind of my own version of a skyblock game, but outside of Minecraft)

This is a Python turtle graphics-based game that allows you to draw shapes and move around using keyboard controls.

https://raw.githubusercontent.com/python/cpython/main/Lib/turtle.py

# Demo

https://test.pypi.org/project/Goldcrescent/0.0.2

## Setup Instructions

### Prerequisites
- Python 3.6 or higher
- On Linux/Ubuntu, you may need to install tkinter: `sudo apt-get install python3-tk`

### Virtual Environment Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Goldcrescent/Blockgame.git
   cd Blockgame
   ```

2. **Set up virtual environment (recommended):**
   ```bash
   python setup_venv.py
   ```

3. **Activate virtual environment:**
   - **Easy way:**
     - **Linux/macOS:**
       ```bash
       source activate.sh
       ```
     - **Windows:**
       ```cmd
       activate.bat
       ```
   - **Manual activation:**
     - **Linux/macOS:**
       ```bash
       source .venv/bin/activate
       ```
     - **Windows:**
       ```cmd
       .venv\Scripts\activate.bat
       ```

4. **Run the game:**
   ```bash
   python main.py
   ```

5. **Deactivate virtual environment when done:**
   ```bash
   deactivate
   ```

### Manual Setup (alternative)

If you prefer to set up manually:

1. Create virtual environment:
   ```bash
   python -m venv .venv
   ```

2. Activate it (see activation commands above)

3. Install dependencies (currently none required):
   ```bash
   pip install -r requirements.txt
   ```

## Game Controls

- **c** - Draw a circle
- **s** - Draw a square  
- **t** - Draw a triangle
- **w** - Move forward
- **a** - Turn left
- **d** - Turn right
- **q** - Quit game

## Requirements

- Python 3.6+
- turtle (included with Python standard library)
- tkinter (usually included with Python, may need separate installation on some Linux distributions)

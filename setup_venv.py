#!/usr/bin/env python3
"""
Setup script for creating and configuring the virtual environment for Blockgame.
"""

import os
import sys
import subprocess
import platform

def run_command(command, description):
    """Run a command and handle errors gracefully."""
    print(f"Running: {description}")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        if result.stdout:
            print(result.stdout)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        if e.stderr:
            print(f"Error output: {e.stderr}")
        return False

def setup_virtual_environment():
    """Set up the virtual environment for the project."""
    print("Setting up Python virtual environment for Blockgame...")
    
    # Check if Python is available
    try:
        python_version = subprocess.check_output([sys.executable, "--version"], text=True).strip()
        print(f"Using {python_version}")
    except subprocess.CalledProcessError:
        print("Error: Python not found!")
        return False
    
    # Create virtual environment
    venv_path = ".venv"
    if os.path.exists(venv_path):
        print(f"Virtual environment already exists at {venv_path}")
    else:
        if not run_command(f"{sys.executable} -m venv {venv_path}", "Creating virtual environment"):
            return False
    
    # Determine activation command based on platform
    if platform.system() == "Windows":
        activate_script = os.path.join(venv_path, "Scripts", "activate.bat")
        pip_path = os.path.join(venv_path, "Scripts", "pip")
    else:
        activate_script = os.path.join(venv_path, "bin", "activate")
        pip_path = os.path.join(venv_path, "bin", "pip")
    
    # Install requirements if the file exists
    if os.path.exists("requirements.txt"):
        print("Installing requirements...")
        if not run_command(f"{pip_path} install -r requirements.txt", "Installing requirements"):
            print("Note: Some requirements may not be needed for this project")
    
    print("\n" + "="*50)
    print("Virtual environment setup complete!")
    print("="*50)
    
    if platform.system() == "Windows":
        print("\nTo activate the virtual environment, run:")
        print(f"  {activate_script}")
        print("\nTo deactivate, run:")
        print("  deactivate")
    else:
        print("\nTo activate the virtual environment, run:")
        print(f"  source {activate_script}")
        print("\nTo deactivate, run:")
        print("  deactivate")
    
    print(f"\nOnce activated, you can run the game with:")
    print("  python main.py")
    
    return True

if __name__ == "__main__":
    success = setup_virtual_environment()
    if not success:
        sys.exit(1)
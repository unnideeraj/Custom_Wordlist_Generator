#!/bin/bash

# Check if Python 3 is installed
if ! command -v python3 &> /dev/null; then
    echo "Python3 not found. Installing Python3..."
    # Install Python3 (update to use apt, yum, or other based on system)
    if [ -x "$(command -v apt)" ]; then
        sudo apt update && sudo apt install -y python3 python3-pip
    elif [ -x "$(command -v yum)" ]; then
        sudo yum install -y python3 python3-pip
    else
        echo "Package manager not supported. Please install Python 3 manually."
        exit 1
    fi
else
    echo "Python3 is already installed."
fi

# Ensure pip is installed
if ! command -v pip &> /dev/null; then
    echo "pip not found. Installing pip..."
    curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
    python3 get-pip.py --user
    rm get-pip.py
fi

# Install required Python packages
echo "Installing required Python packages..."
pip3 install --user art pyfiglet itertools

# Make script executable
chmod +x wordlist_generator.py

# Install the package with setuptools
echo "Installing the Python package..."
pip3 install .

# Ask if the user wants to add the directory to PATH
read -p "Do you want to add this directory to PATH? (y/n): " add_to_path
if [ "$add_to_path" == "y" ]; then
    current_dir=$(pwd)
    # Check if directory is already in PATH
    if [[ ":$PATH:" == *":$current_dir:"* ]]; then
        echo "Directory is already in PATH."
    else
        # Add to PATH in .bashrc
        echo "export PATH=\$PATH:$current_dir" >> ~/.bashrc
        source ~/.bashrc
        echo "Directory added to PATH. Please restart your terminal or run 'source ~/.bashrc'."
    fi
else
    echo "Directory was not added to PATH."
fi

echo "Setup complete!"

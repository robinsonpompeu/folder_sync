#!/bin/bash
#==================================================================================
#
# FILE: gen-docs.sh
#
# USAGE: gen-docs.sh
#
# DESCRIPTION: Linux shell script to generate project documentation files.
# 
#==================================================================================

# Terminate if some error occurs
set -e

# Local variables
VENV=".venv_folder_sync"

# Creates and activates virtual environment
python3 -m venv "$VENV"
source "$VENV"/bin/activate

# Install dependencies listed in requirements.txt file
python3 -m pip install --upgrade pip
python3 -m pip install --no-cache-dir -r requirements.txt
python3 -m pip install --editable .

# Configure project documentation
sphinx-quickstart -q \
    --sep \
    -p "Folder Monitoring and Synchronization" \
    -a "Robinson Pompeu" \
    -v "0.1.0" \
    --ext-autodoc \
    --ext-todo \
    --ext-viewcode \
    docs
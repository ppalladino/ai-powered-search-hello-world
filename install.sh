#!/bin/bash

# Create and activate virtual environment
python3 -m venv venv
source ./venv/bin/activate

# Upgrades package manager and installs dependencies
pip install --upgrade pip
pip install -r requirements.txt

# Creates a local config to put your API key in
touch .env
grep -qF 'OPENAI_API_KEY' .env || echo 'OPENAI_API_KEY=' >> .env

# Done!
echo "Install...done 2222."
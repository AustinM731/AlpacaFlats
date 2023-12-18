#!/bin/bash

APP_DIR="/opt/ASCOM"
SERVICE_NAME="AlpacaFlats"
PYTHON_SCRIPT="app.py"
REQUIREMENTS_FILE="requirements.txt"
GITHUB_REPO="https://github.com/AustinM731/AlpacaFlats.git"

# Extract Git directory name
GIT_DIR_NAME=$(basename -s .git "$GITHUB_REPO")
GIT_CLONE_DIR="$APP_DIR/$GIT_DIR_NAME"
VENV_DIR="$GIT_CLONE_DIR/venv"

# Installation of Python and virtualenv
apt-get update
apt-get install -y python3 python3-venv git

# Create application directory and clone the repo
mkdir -p $APP_DIR
git clone $GITHUB_REPO $GIT_CLONE_DIR

# Set up Python virtual environment
if [ ! -d "$VENV_DIR" ]; then
    python3 -m venv $VENV_DIR
fi
$VENV_DIR/bin/pip install -r $GIT_CLONE_DIR/$REQUIREMENTS_FILE

# Create a systemd service file
SERVICE_FILE="/etc/systemd/system/$SERVICE_NAME.service"
echo "[Unit]
Description=ASCOM Alpaca driver for Flat Panel Calibrator Device
After=network.target

[Service]
Type=simple
ExecStart=$VENV_DIR/bin/python $GIT_CLONE_DIR/Alpaca/$PYTHON_SCRIPT
Restart=on-failure

[Install]
WantedBy=multi-user.target" | sudo tee $SERVICE_FILE

# Reload systemd to include new service, then start and enable it
systemctl daemon-reload
systemctl start $SERVICE_NAME
systemctl enable $SERVICE_NAME

echo "Installation complete. Service $SERVICE_NAME started."


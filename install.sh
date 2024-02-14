#!/bin/bash

# Set your project details
PROJECT_DIR="/path/to/your/project"
VENV_DIR="./venv"
INI_FILE="/etc/systemd/system/ci_runner.service"
USER="root"
GROUP="root"

python3 -m venv venv
source venv/bin/activate
pip install -r $PROJECT_DIR/requirements.txt

cat <<EOL >$INI_FILE
[Unit]
Description=Your FastAPI Project

[Service]
ExecStart=venv/bin/uvicorn main:app --host 0.0.0.0 --port 60414
WorkingDirectory=$PROJECT_DIR
User=$USER
Group=$GROUP
Restart=always

[Install]
WantedBy=multi-user.target
EOL

# Reload systemd
systemctl daemon-reload
systemctl start ci_runner
systemctl enable ci_runner

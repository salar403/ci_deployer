#!/bin/bash

# Set your project details
apt-get install python3-venv

PROJECT_DIR="/path/to/your/project"
VENV_DIR="./venv"
INI_FILE="/etc/systemd/system/ci_deployer.service"
USER="root"
GROUP="root"
ENV_FILE="$PROJECT_DIR/.env"  # Path to your .env file

python3 -m venv venv
source venv/bin/activate
https_proxy=http://fodev.org:8118 pip install -r $PROJECT_DIR/requirements.txt

if [ -f "$ENV_FILE" ]; then
    python -m pip install python-dotenv
    python -c "from dotenv import load_dotenv; load_dotenv('$ENV_FILE')"
fi

cat <<EOL >$INI_FILE
[Unit]
Description=Your FastAPI Project

[Service]
ExecStart=$PROJECT_DIR/venv/bin/uvicorn app.main:app --host 0.0.0.0 --port 60414
WorkingDirectory=$PROJECT_DIR
User=$USER
Group=$GROUP
Restart=always

[Install]
WantedBy=multi-user.target
EOL

# Reload systemd
systemctl daemon-reload
systemctl start ci_deployer
systemctl enable ci_deployer

#!/bin/bash

# 1. Kill all existing tmux sessions
tmux kill-server 2>/dev/null || true

# 2. cd into project folder
cd /root/MLH-portfolio

# 3. Pull latest changes from GitHub
git fetch && git reset origin/main --hard

# 4. Enter virtual environment and install dependencies
source python3-virtualenv/bin/activate
pip install -r requirements.txt

# 5. Start a new detached tmux session that runs the Flask server
tmux new-session -d -s flask -c /root/MLH-portfolio \
  'source python3-virtualenv/bin/activate && flask run --host=0.0.0.0'

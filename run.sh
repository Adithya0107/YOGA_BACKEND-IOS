#!/bin/bash
if [ -d ".venv" ]; then
    source .venv/bin/activate
fi
pip install -r requirements.txt
python3 main.py

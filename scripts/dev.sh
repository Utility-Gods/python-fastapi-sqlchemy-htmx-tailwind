#!/bin/bash

# Start Tailwind in the background
./scripts/watch-css.sh &
TAILWIND_PID=$!

# Set Python path
export PYTHONPATH=$PYTHONPATH:$(pwd)

# Start uvicorn
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

# When uvicorn exits, kill Tailwind
kill $TAILWIND_PID 
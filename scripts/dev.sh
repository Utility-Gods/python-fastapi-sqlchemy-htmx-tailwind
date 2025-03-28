#!/bin/bash

# Function to cleanup processes on exit
cleanup() {
    echo "Cleaning up processes..."
    # Kill the entire process group
    kill 0
    exit
}

# Set up trap to catch exit signals
trap cleanup EXIT SIGINT SIGTERM

# Start Tailwind in the background with its own process group
./scripts/watch-css.sh &

# Set Python path
export PYTHONPATH=$PYTHONPATH:$(pwd)

# Start uvicorn
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000 
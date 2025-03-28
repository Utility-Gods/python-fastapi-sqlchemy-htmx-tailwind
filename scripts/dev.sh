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


# Set Python path
export PYTHONPATH=$PYTHONPATH:$(pwd)

# Start uvicorn with additional watch directories
uvicorn app.main:app \
    --reload \
    --reload-dir app/templates \
    --reload-dir app/static \
    --host 0.0.0.0 \
    --port 8000 
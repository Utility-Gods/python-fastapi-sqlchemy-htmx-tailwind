#!/bin/bash

# Run Tailwind CLI in watch mode with polling
./bin/tailwindcss \
    -i ./app/static/css/input.css \
    -o ./app/static/css/output.css \
    --watch \
    --poll \
    --verbose 
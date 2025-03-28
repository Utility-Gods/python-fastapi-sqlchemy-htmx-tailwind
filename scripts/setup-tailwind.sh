#!/bin/bash

# Define variables
TAILWIND_VERSION="v3.4.1"
OS=$(uname -s | tr '[:upper:]' '[:lower:]')
ARCH=$(uname -m)

# Map architecture names
case $ARCH in
    x86_64)
        ARCH="x64"
        ;;
    aarch64|arm64)
        ARCH="arm64"
        ;;
esac

# Create bin directory if it doesn't exist
mkdir -p bin

# Download Tailwind binary
echo "Downloading Tailwind CLI..."
curl -sLO "https://github.com/tailwindlabs/tailwindcss/releases/download/${TAILWIND_VERSION}/tailwindcss-${OS}-${ARCH}"

# Make it executable and move to bin
chmod +x "tailwindcss-${OS}-${ARCH}"
mv "tailwindcss-${OS}-${ARCH}" bin/tailwindcss

echo "Tailwind CLI installed successfully!" 
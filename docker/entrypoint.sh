#!/bin/bash

echo "Starting MS3D container setup..."

# Move to the /MS3D directory
cd /MS3D

# Run the required setup commands
echo "Running Python setup..."
python setup.py develop

echo "Installing tracker dependencies..."
cd tracker
pip install -e . --user

# Return to the /tools directory
cd ../tools/

echo "Setting up Git safe directory..."
git config --global --add safe.directory /MS3D


# Execute the default command or keep the container running
exec "$@"

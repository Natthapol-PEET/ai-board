#!/bin/bash

# # Set a variable
# greeting="Hello, World!"
# name="Natthapol"

# # Print a message to the console
# echo $greeting

# # Use conditions
# if [ "$name" == "Natthapol" ]; then
#   echo "Welcome, $name!"
# else
#   echo "Who are you?"
# fi

# # Loop through a list
# for



# chmod +x install.sh
# ./install.sh


# Download source code
cd /home/jetson/Desktop
git clone https://github.com/Natthapol-PEET/ai-board.git

# Change directory
cd /home/jetson/Desktop/ai-board

# Install nanomq
cd nanomq-docker
./go buildNanoMQ
./go runNanoMQ
cd ..

# Install opencv
cd opencv-app
./go pullDependency
./go deployApp

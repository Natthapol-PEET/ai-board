#!/bin/bash

# echo "🔧 1. ติดตั้งบนทุกเครื่องที่อยากให้เชื่อมกัน"
# curl -fsSL https://tailscale.com/install.sh | sh
# echo "🔐 2. Login เข้า Tailscale"
# sudo tailscale up
# echo "📡 3. ดู IP Tailscale ของเครื่อง"
# tailscale ip
# sudo tailscale down


if ! command -v sudo docker version &> /dev/null; then
    sudo apt update && sudo apt upgrade -y
    curl -sSL https://get.docker.com | sh
    sudo usermod -aG docker pi
    echo "✅ Install docker successfully."
else
    echo "✅ Docker is already installed."
fi

cd /home/pi/Desktop
if [ -d "ai-board" ]; then
    cd ai-board
    git pull
    cd ..
else
    git clone https://github.com/Natthapol-PEET/ai-board.git
fi
echo "✅ Download source-code successfully."

cd /home/pi/Desktop/ai-board
echo "🟡 Go to folder ai-board"

cd nanomq-docker
./go buildNanoMQ
echo "✅ Install nanomq successfully."

./go runNanoMQ
echo "✅ Running nanomq successfully."

cd ..
echo "🟡 Back to folder ai-board"

cd opencv-app
./go pullDependency
echo "✅ Running dependency successfully."

./go deployApp
echo "✅ Running app successfully."

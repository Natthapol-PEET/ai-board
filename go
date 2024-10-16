#!/usr/bin/env bash

set -e
TASK=$1
ARGS=${@:2}


help__scp="docker build nanomq image"
task_scp() {
  IP=192.168.195.239

  scp install.sh jetson@192.168.243.239:/home/jetson/Desktop/install.sh

  # scp requirements.txt \
  #   .env  \
  #   go  \
  #   Dockerfile.python \
  #   .dockerignore \
  #   jetson@192.168.195.239:/home/jetson/Desktop/ai-board
  # echo "|-----------------------------|"

  # scp -r src jetson@192.168.195.239:/home/jetson/Desktop/ai-board/src
  # echo "|-----------------------------|"

  # scp -r docker jetson@192.168.195.239:/home/jetson/Desktop/ai-board/docker
  # echo "|-----------------------------|"

  # # Script
  # scp -r script jetson@192.168.195.239:/home/jetson/Desktop/ai-board/script
  # echo "|-----------------------------|"


  # scp test/service/camera_test.py jetson@192.168.195.239:/home/jetson/Desktop/ai-board/src
  # scp test/service/api_client_test.py jetson@192.168.195.239:/home/jetson/Desktop/ai-board/src
  

  # scp -r ../ai-board jetson@192.168.195.239:/home/jetson/Desktop/ai-board
  # echo "|-----------------------------|"

  # jetson
}


## main
list_all_helps() {
  compgen -v | egrep "^help__.*"
}

NEW_LINE=$'\n'
if type -t "task_$TASK" &>/dev/null; then
  task_${TASK} ${ARGS}
else
  echo "usage: $0 <task> [<..args>]"
  echo "task:"

  HELPS=""
  for help in $(list_all_helps); do

    HELPS="$HELPS    ${help/help__/} |-- ${!help}$NEW_LINE"
  done

  echo "$HELPS" | column -t -s "|"
  exit 1
fi

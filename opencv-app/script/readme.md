

## Copy script to systemd
sudo cp script/ai_board.service /etc/systemd/system/ai_board.service

## Enable and start the service
sudo systemctl enable ai_board.service
sudo systemctl start ai_board.service

sudo systemctl restart ai_board.service

## Check the status of the service
sudo systemctl status ai_board.service


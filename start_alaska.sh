#!/bin/bash
# need chmod +
sudo docker compose up -d;
sleep 2s;
pytest tests/test_box.py -v >> result.txt;
sudo docker stop $(sudo docker ps -a -q);
sudo docker rm $(sudo docker ps -a -q);
sudo docker rmi $(sudo docker images --format="{{.Repository}} {{.ID}}" |
                  grep "^azshoo/alaska" | cut -d' ' -f2);
sudo rm -r dump/;
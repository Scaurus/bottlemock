#!/usr/bin/env bash
sudo docker run --name mock -p 7777:7777 -v /home/rzhuravskiy/www/mock/:/app/log/:rw -d bottlemock
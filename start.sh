#!/bin/sh

. ./config.sh

BOTCMD="python3 botalan.py"

echo "enter token:"
read -r TOKEN
TOKEN="$TOKEN" tmux -L $TMUX_SOCKET new -s $TMUX_SESSION -d $BOTCMD

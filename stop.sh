#!/bin/sh

TMUX_SOCKET="botalan"
TMUX_SESSION="$TMUX_SOCKET"

tmux -L botalan kill-session -t botalan

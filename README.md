# botalan

botalan is a Discord bot written in Python. It is very basic, but more
features may be added later.
[Name origin](https://youtu.be/_swLxZu-exU).

## Commands

* `!fortune`: print fortune from system `fortune(1)`.
* `!cowsay <msg>`: print given string using system `cowsay(1)`.
* `!cowfortune`: print result of `fortune | cowsay`.
* `!tweet`: print a random Twitter shitpost from a bank.

## Dependencies

* tmux
* [discord.py](https://discordpy.readthedocs.io/en/stable/)

## Usage

Obtain a bot token, then run `start.sh` and enter the token. To stop,
run `stop.sh`.

## Bugs

Shell injections are possible currently. This must be addressed.

## License

Copyright (C) 2021 Ben O'Neill <ben@oneill.sh>. License: MIT.
See LICENSE for more details.

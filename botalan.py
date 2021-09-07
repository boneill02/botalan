import discord
import os
import cmd

TOKEN = os.getenv("TOKEN")

client = discord.Client()

def exec_cmd(msg):
    response = ''
    msg = msg.strip()
    if msg == '!tweet':
        response = cmd.tweet()

    if msg.startswith('!fortune'):
        if len(msg.split()) > 1:
            arg = msg.split()[1]
            print(arg)
            print(len(arg))
            response = cmd.fortune(arg)
        response = cmd.fortune()

    if msg.startswith('!cowsay ') and len(msg) > len('!cowsay '):
        index = msg.index(' ') + 1
        arg = None
        if msg[index] == '-':
            arg = msg[index + 1:].split()[0]
            cowmsg = msg[index + len(arg) + 1:]
        else:
            cowmsg = msg[index:]
        response = cmd.cowsay(arg, cowmsg)

    if msg == ('!cowfortune'):
        response = cmd.cowfortune()

    return response

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    response = exec_cmd(message.content)
    await message.channel.send(response)

if TOKEN == None:
    print("Running in test mode")
    while True:
        msg = input("user> ")
        response = exec_cmd(msg)
        print(response)
else:
    client.run(TOKEN)

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
    if msg == '!fortune':
        response = cmd.fortune()
    if msg.startswith('!cowsay ') and len(msg) > len('!cowsay '):
        index = msg.index(' ') + 1
        cowmsg = msg[index:]
        response = cmd.cowsay(cowmsg)
    if msg == ('!cowfortune'):
        response = cmd.cowfortune()

    return response

@client.event
async def on_ready():
    print('bot alan has entered the discord realm')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    response = exec_cmd(message.content)
    await message.channel.send(response)

# bot code can run without connecting to Discord for testing
if TOKEN == None:
    print("Running in test mode")
    while True:
        msg = input("user> ")
        response = exec_cmd(msg)
        print(response)
else:
    client.run(TOKEN)

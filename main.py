import discord

PREFIX = '!!'
CHANNEL_NAME = ''

client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    print('Message received from {0.author} : {0.content}'.format(message))

    if message.author == client.user:
        return

    if not message.content.startswith(PREFIX):
        return

    command = message.content[2:].lower()
    channel = message.channel

    if CHANNEL_NAME == '' and not command.startswith('bind'):
        await channel.send('I am not bound to a channel yet. Bind me using `!!bind <server-name>`')

    if command == 'help':
        await show_help(channel)
    elif command.startswith('bind'):
        await bind_to_channel(channel, command)
    elif command.startswith('start'):
        await start_game(channel, command)
    elif command == 'join':
        await join_game(channel)
    elif command.startswith('name'):
        await give_name(channel, command)
    elif command == 'stop':
        await stop_game(channel)
    elif command == 'high':
        await show_high_score(channel)
    elif command == 'last':
        await show_last_input(channel)
    elif command == 'now':
        await show_current_player(channel)
    elif command.startswith('add'):
        await add_to_list(channel, command)


async def show_help(channel):
    pass


async def bind_to_channel(channel, command):
    pass


async def start_game(channel, command):
    pass


async def join_game(channel):
    pass


async def give_name(channel, command):
    pass


async def stop_game(channel):
    pass


async def show_high_score(channel):
    pass


async def show_last_input(channel):
    pass


async def show_current_player(channel):
    pass


async def add_to_list(channel, command):
    pass

client.run('')

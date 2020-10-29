import discord

PREFIX = '!!'
BOUND_CHANNEL = None

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

    if BOUND_CHANNEL is None and not command.startswith('bind'):
        return await channel.send('I am not bound to a channel yet. Bind me using `!!bind <server-name>`')

    if BOUND_CHANNEL is not None and channel != BOUND_CHANNEL:
        return await BOUND_CHANNEL.send("Send you're message here please!")

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
    channel_name = command.split()[1]
    guild = channel.guild
    if guild is None:
        return await channel.send("I don't work with DM's. Sorry!")

    guild_channels = guild.channels
    print(guild_channels)
    names = [i.name for i in guild_channels]
    print(names)
    to_bind = next((i for i in guild_channels if i.name == channel_name), None)
    print(to_bind)
    if to_bind is None:
        return await channel.send('Channel {0} does not exist'.format(channel_name))

    await channel.send('Binding myself to channel {0}'.format(channel_name))
    global BOUND_CHANNEL
    BOUND_CHANNEL = to_bind
    print(BOUND_CHANNEL)


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

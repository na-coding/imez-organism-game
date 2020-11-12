import discord

PREFIX = '!!'
BOUND_CHANNEL = None

client = discord.Client()
game_started = False
player_list = []
player_started = None
current_player_index = 0


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

    # if BOUND_CHANNEL is None and not command.startswith('bind'):
    #     return await channel.send('I am not bound to a channel yet. Bind me using `!!bind <server-name>`')
    #
    # if BOUND_CHANNEL is not None and channel != BOUND_CHANNEL:
    #     return await BOUND_CHANNEL.send("Send you're message here please!")

    if command == 'help':
        await show_help(channel)
    # elif command.startswith('bind'):
    #     await bind_to_channel(channel, command)
    elif command.startswith('start'):
        await start_game(message, command)
    elif command == 'join':
        await join_game(message)
    elif command.startswith('name'):
        await give_name(message, command)
    elif command == 'stop':
        await stop_game(message)
    elif command == 'high':
        await show_high_score(channel)
    elif command == 'last':
        await show_last_input(channel)
    elif command == 'now':
        await show_current_player(channel)
    elif command.startswith('add'):
        await add_to_list(channel, command)


async def show_help(channel):
    help_str = '```\n' \
              'Thanks for using the IMEZ Organism Game bot!\n' \
              'My commands are:\n' \
              '!!help - get commands list\n' \
              '!!start - start a game\n' \
              '!!join - join a game that has started\n' \
              '!!stop - force stop the current game\n' \
              '!!name <name> - input organism name\n' \
              '!!high - check the server high score\n' \
              '!!last - check the last player and the name they gave\n' \
              '!!now - check the current player\n' \
              '!!add - add to list of animals to be reviewed by the mods\n' \
              '```'

    return await channel.send(help_str)


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


async def start_game(message, command):
    global game_started, player_started
    if game_started:
        return await message.channel.send('The game has already started!')

    member = message.author
    player_list.append(member.id)

    game_started = True
    player_started = member.id
    return await message.channel.send('<@{0}> has started a game!'.format(member.id))


async def join_game(message):
    if not game_started:
        return await message.channel.send('The game has not started yet! Start a game with `!!start`')

    member = message.author

    if member.id in player_list:
        return await message.channel.send('You are already part of the game!')

    player_list.append(member.id)
    return await message.channel.send('<@{0}> has joined the game!'.format(member.id))


async def give_name(message, command):
    if not game_started:
        return await message.channel.send('The game has not started yet! Start a game with `!!start`')

    member = message.author
    member_display_name = member.display_name

    organism_name = command.split()[1]
    return await message.channel.send('@{0}: @{1}'.format(member_display_name, organism_name))


async def stop_game(message):
    global player_list, game_started
    channel = message.channel

    if not game_started:
        return await channel.send('The game has not started yet! Start a game with `!!start`')

    if player_started != message.author.id:
        return await channel.send('Only the player who started the game can end it :)')

    player_list = []
    game_started = False

    return await channel.send('The game has ended!')


async def show_high_score(channel):
    pass


async def show_last_input(channel):
    pass


async def show_current_player(channel):
    if not game_started:
        return await channel.send('The game has not started yet! Start a game with `!!start`')

    current_player = player_list[current_player_index]
    return await channel.send('Current player to give name is <@{0}>'.format(current_player))


async def add_to_list(channel, command):
    pass

client.run('')

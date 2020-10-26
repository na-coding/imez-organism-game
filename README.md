# imez-organism-game
Organism game bot for IMEZ Discord server

Bot made by: someCodingBoy / it-is-i-nigel#5474

Game designed by: Oravelos

IMEZ's Organisms is a game bot created for the entertrainment of the Intellectual Minds of Ecology and Zoology Discord server.
It is a game where members have to input a name of an organism, whether a plant, animal, fungi, etc. while using the last letter
of the last organism. The goal of the game is to name as many organisms as possible while sticking to the rules.

##Rules
1. Player may input a name of an animal, plant, fungi or any organism.
2. Player may input either the common name or scientific name of the organism, but each organism may only be named once.
3. Breeds may be used as well.
4. Names must start with the last letter of the last name inputted.


##Setup
1. Invite the bot to the server
2. Bind the bot to a channel with !!bind <server-name>
3. Start game with !!start or join a game with !!join
4. Current player will give a name with !!name
5. Game will stop if a player gives a name that does not start with the last letter of the last organism name, or with !!stop

##Commands
* !!help - shows the commands
* !!bind <server-name> - binds the bot to a specific channel
* !!start - starts a game if there isn't any active ones
* !!start flora - starts a flora only game (players can only name flora species)
* !!start fauna - starts a fauna only game (players can only name fauna species)
* !!join - join active game if there is any
* !!name <organism-name> - gives a name
* !!stop - force stops the current active game if there is any
* !!high - check the highscore
* !!last - check the last player to give a name and what name they gave
* !!now - check the current player
* !!add <name> <link> -adds species to request list. Mods will verify and add to database of organisms
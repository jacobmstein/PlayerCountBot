# PlayerCountBot
Discord bot to display a Steam server's player count via its presence message.

## Example
![Example](https://raw.githubusercontent.com/jacobmstein/PlayerCountBot/8ef0766d02894d5e53d66ae4299d621d2a480dae/example.png)

## Installation
1. Verify you have [Python 3.6](https://www.python.org/downloads/) installed (unfortunately, [discord.py](https://github.com/Rapptz/discord.py) does not support Python 3.7).
2. Clone (`git clone https://github.com/jacobmstein/PlayerCountBot.git`) or [download](https://github.com/jacobmstein/PlayerCountBot/archive/master.zip) this repository.
3. [Create a Discord application](https://discordapp.com/developers/applications/me/create) and retrieve your bot token.
4. Invite your bot to your Discord server by generating an OAuth2 URL.
5. Open `config.py` in your preferred text editor and set your bot token and server address.
6. Install the necessary packages using pip, `pip install -r requirements.txt`.
7. Run the bot using `python bot.py`. (If Python 3.6 isn't your default version of Python you may have to run `python3.6 bot.py` or something similar.)
8. Optionally, create a separate role for your bot with the "Display role members separately from online members" option enabled for better effect.

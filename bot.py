import asyncio
import config
import discord
import valve.source.a2s

client = discord.Client()

async def update_player_count():
    while not client.is_closed:
        await client.wait_until_ready()
        try:
            with valve.source.a2s.ServerQuerier(config.SERVER_ADDRESS) as server:
                await client.change_presence(
                    game=discord.Game(
                        name=f"{server.info()['player_count']} players online!"))
        except valve.source.NoResponseError:
            pass

        await asyncio.sleep(3)

client.loop.create_task(update_player_count())
client.run(config.BOT_TOKEN)

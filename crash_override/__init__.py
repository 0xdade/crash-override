import discord
from discord.ext.commands import Bot
from crash_override.shodan.command import Shodan

from crash_override.config import COMMAND_PREFIX


class CrashOverride(Bot):
    def __init__(self, *args, **kwargs):
        intents = discord.Intents.default()
        intents.typing = False
        intents.presences = False
        intents.message_content = True
        super().__init__(COMMAND_PREFIX, intents=intents, **kwargs)

    async def setup(self):
        await self.add_cog(Shodan(self))

    async def on_ready(self):
        print("Logged on as", self.user)

    async def on_message(self, message):
        if self.user == message.author:
            return

        if message.content == "ping":
            await message.channel.send("pong")
        await super().on_message(message)

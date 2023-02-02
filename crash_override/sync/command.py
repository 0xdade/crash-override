import os
from discord.ext import commands


class Sync(commands.Cog):
    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{self.__cog_name__} loaded")

    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.owner = int(os.environ.get("DISCORD_OWNER_ID"))

    @commands.command("sync")
    async def sync(self, ctx: commands.Context):
        if ctx.author.id != self.owner:
            await ctx.send("Access denied")
            return
        await self.bot.tree.sync()
        await ctx.send("Sync command executed")

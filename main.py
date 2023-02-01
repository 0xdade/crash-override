#!/usr/bin/env python3

import asyncio
import os

from dotenv import load_dotenv

from crash_override import CrashOverride

load_dotenv()

DISCORD_TOKEN = os.environ.get("DISCORD_TOKEN")

bot = CrashOverride()


@bot.event
async def on_ready():
    await bot.tree.sync()
    print("Ready!")


asyncio.run(bot.setup())
print(list(bot.commands)[0].name)
bot.run(DISCORD_TOKEN)

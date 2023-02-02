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
    print("Ready!")


asyncio.run(bot.setup())
bot.run(DISCORD_TOKEN)

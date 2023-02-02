import os
import ipaddress

import discord
from discord.ext import commands
from discord import app_commands
import shodan

from crash_override.shodan.models import ShodanHostResponse


class Shodan(commands.Cog):
    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{self.__cog_name__} loaded")

    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.api_key = os.environ.get("SHODAN_KEY")

    @app_commands.command(name="shodan", description="Lookup an IP address on Shodan")
    async def shodan_host_lookup(self, interaction: discord.Interaction, ip: str):
        try:
            ip = ipaddress.ip_address(ip)
        except ValueError:
            await interaction.response.send_message(
                f"{ip} does not appear to be a valid IP address"
            )
            return
        api = shodan.Shodan(self.api_key)
        host_data = ShodanHostResponse(**api.host(str(ip), minify=True))
        await interaction.response.send_message(self.format_host_output(host_data))

    def format_host_output(self, output: ShodanHostResponse):
        return f"""IP: {output.ip_str}
ISP: {output.isp}
Ports: {output.ports}
Domains: {output.domains}
Org: {output.org}
ASN: {output.asn}
"""

"""
A python script that logs Discord DMs on a user account.

Author: scrazzz
License: MIT
Version: v0.3.0
"""

import dhooks
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!', self_bot=True)

# Make a webhook in a server where you want to log. Replace with your webhook url.
log = dhooks.Webhook("URL")

@bot.event
async def on_message(m):
    # ignore messages in servers.
    if m.guild is None:
        
        # ignore messages sent by us in dms.
        # also ignore dms we get from bot accounts.
        if m.author == bot.user or m.author.bot:
            return
        
        embed = dhooks.Embed(title=f"{m.author} ({m.author.id})")
        embed.description = m.content
        await log.send(embed=embed)
    
    await bot.process_commands(m)
    
bot.run("TOKEN", bot=False)

import asyncio

import dhooks
import discord
import aiohttp
from discord.ext import commands

__author__ = "scrazzz"
__license__ = "MIT"
__version__ = "0.5.0"
__maintainer__ = "scrazzz"

bot = commands.Bot(command_prefix='!', self_bot=True, help_command=None)
bot.session = aiohttp.ClientSession(loop=bot.loop)

# Make a webhook in a server where you want to log
# to and replace with your webhook url.
log = dhooks.Webhook.Async("URL")

async def upload_image(file):
    """This is for only logging file types of: png, jpg, jpeg, gif, ico, bmp, tif, tiff, and webm."""
    async with bot.session.get(file) as resp:
        bytes = await resp.read()
        
        data = {
            'image': bytes
            'noembed': 'a-void'
        }
        async with bot.session.post("https://sxcu.net/upload", data=data) as post:
            js = await post.json()
            url = js['url']
            return url

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
        
        # we also need to log attachments.
        for attach in m.attachments:
            url = await upload_image(attach.proxy_url)
            embed.add_field(name="\u200b", value=url, inline=False)
            
        await log.send(embed=embed)
        await log.close()
        
    await bot.process_commands(m)

# replace TOKEN with your user token.
bot.run("TOKEN", bot=False)

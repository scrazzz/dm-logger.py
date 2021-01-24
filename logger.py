"""
A python script that logs Discord DMs on a user account.

Author: scrazzz
License: MIT
Version: v0.4.0
"""

import dhooks
import asyncio
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!', self_bot=True)

# Make a webhook in a server where you want to log. Replace with your webhook url.
log = dhooks.Webhook("URL")

# to log images and gifs ONLY.
async def upload_image(img):
    async with aiohttp.ClientSession() as sess:
        data = {
            'key': '232565fc1a4f0d24578d9aeadc0b43ab', # you can use this or get your own api key from https://api.imgbb.com
            'image': img
        }
        async with sess.post("https://api.imgbb.com/1/upload", data=data) as post:
            js = await post.json()
            
            try:
                url = js['data']['url']
                return url
                
            # sometimes, very rarely it just wont upload
            # so we ignore that.
            # But make sure the API key is working or not.
            except:
                pass
            
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
                
        log.send(embed=embed)
    
    await bot.process_commands(m)
    
bot.run("TOKEN", bot=False)

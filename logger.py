import dhooks
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!', self_bot=True)
log = dhooks.Webhook.Async("URL") # Make a webhook in a server where you want to log. Replace with your webhook url.

@bot.event
async def on_message(m):
    if m.author == bot.user or m.author.bot: # Ignore our messages and bot messages.
        return
        
    embed = dhooks.Embed(title=f"{m.author} ({m.author.id})")
    embed.description = m.content
    await log.send(embed=embed)
    
    await bot.process_commands(m)
    
bot.run("TOKEN", bot=False)

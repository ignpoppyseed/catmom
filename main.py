import discord
import random
from discord_slash import SlashCommand, SlashContext
from discord_slash.utils.manage_commands import create_choice, create_option
from discord.ext import commands
from discord import guild
from bottoken import TOKEN
from affectedusers import userList

# Initialize Bot and Denote The Command Prefix
bot = commands.Bot(case_insensitive=True, command_prefix="c>",activity = discord.Activity(type=discord.ActivityType.watching, name="her daughter grow up <3"), status=discord.Status.online)
slash = SlashCommand(bot, sync_commands=True)
bot.remove_command('help') #disables the built in help command

# Runs when Bot Succesfully Connects
@bot.event
async def on_ready():
    print(f'{bot.user} succesfully logged in!')

@bot.event
async def on_message(message):
    # Make sure the Bot doesn't respond to it's own messages
    if message.author == bot.user: 
        return
    
    if 'badword' in message.content.lower():
        if message.author.id in userList:
            await message.channel.send(f'{message.author.mention} Hey! Don\'t say that!')
            print(f'{message.author} said: {message.content}')
        else:
            pass

bot.run(TOKEN)
import discord
from discord.ext import commands
import random
import os
import asyncio
import aiohttp
from discord import Game
from discord.ext.commands import Bot
import time

bot = commands.Bot(command_prefix= '?')

@bot.event
async def on_ready():
    await bot.change_presence(game=discord.Game(name="Type '?help' for commands!")) 

@bot.command(name='love',
	description="A little bit of sprinkles for your sundae <3",
	brief="The name is all you need to know ;)",
	pass_context=True)
async def love(context):
    possible_responses = [
        "Wowowowow you're so cute awwww.",
        "I can't even believe what I'm seeing, literal beauty.",
        "People say perfection doesn't exist, at least until they saw you",
        "Y'know, I just can't seem to stop talking to you. Not all addictions are bad though.",
	"You ever look in a mirror and your reflection winks at you? Of course you have, it's everytime.",
	"``God looked down and said, 'What can I do to make you better?' Little did he know there was nothing he could do, you were already perfect.``",
	"Your smile is like sugar; it makes me all giddy and excited.",
	"A kiss of yours is sweeter than honey and softer than foam, yet I feel the force of love like a bullet.",
    ]
await bot.say(random.choice(possible_responses))

@bot.command()
async def dense():
	await bot.say("https://image.ibb.co/gR9w88/dense.jpg")
	
@bot.command()
async def lwi():
	await bot.say("https://image.ibb.co/kXHSFo/live_withit.jpg")
	
@bot.command()
async def no():
	await bot.say("https://image.ibb.co/kOUf5o/no.png")
	
@bot.command(name='whois',
	description="Who's the cutest of em all?",
	brief="Cuteness contest :)",
	pass_context=True)
async def whois(context):
    possible_responses = [
        "Queen",
        "Ally",
        "Skull",
	"Sen",
	"Ayu",
	"Bran",
	"June",
	"Ther",
	"Cleviee",
	"(That one girl who burped on Rabbit who's probably really cute)",
    ]
    await bot.say(random.choice(possible_responses) + " is the cutest, of course!")
	
@bot.command(name='art',
	brief="Use it, it's better.",
	pass_context=True)
async def art():
	await bot.say("https://upload.wikimedia.org/wikipedia/commons/3/34/Florida_Box_Turtle_Digon3.jpg")

bot.run ('NDQ4MzI3MDk3NjUyMzQ2ODkw.DeUizg.DKqE4V8RoaGIR2yvus0R4fKlfys')
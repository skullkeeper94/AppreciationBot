import discord
from discord.ext import commands
import random
import os
import asyncio
import aiohttp
from discord import Game
from discord.ext.commands import Bot
import time

bot = commands.Bot(command_prefix= '.')

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
	"``God looked down and said, "What can I do to make you better?" Little did he know there was nothing he could do.``",
    ]
    await bot.say(random.choice(possible_responses))
	
@bot.command(name='birthday',
	description="Someone's getting marrie- I mean...",
	brief="HAPPY BIRFDAY")
async def birthday():
	await bot.say("Fifteen, huh? That's pretty neat honestly. You've made it through **180** months of life starting today. Every second of doubt, hardship, or failure and you're managed to stick through it all. You've brought others up and made the most of their life to this moment the happiest and most cherrished memories. I can't do much besides with words, sorry ;l either or, we love you, okay? You may think you sleep in the shadows but it's obviously the opposite, look at everything everyone has done for you today, how many smiles you bring, everything you do is something we love deeply. I mean, two whole servers contributed to a simple two-worded statement because we care. So, uh, I hope you enjoyed your fifteenth birthday Ally, and for many more to come.")
	 
@bot.command(name='art',
	brief="Use it, it's better.",
	pass_context=True)
async def art():
	await bot.say("https://upload.wikimedia.org/wikipedia/commons/3/34/Florida_Box_Turtle_Digon3.jpg")

@bot.command()
async def dense():
	await bot.say("https://image.ibb.co/gR9w88/dense.jpg")
	
@bot.command()
async def lwi():
	await bot.say("https://image.ibb.co/kXHSFo/live_withit.jpg")

bot.run ('NDQ4MzI3MDk3NjUyMzQ2ODkw.DeUizg.DKqE4V8RoaGIR2yvus0R4fKlfys')

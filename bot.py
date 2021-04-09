
import discord
from discord.ext import commands
from numpy.random import choice
import asyncio
import time
PREFIX = ("!")
bot = commands.Bot(command_prefix=PREFIX, description='preefix')
(print('Logged in as {0.user}'.format(bot))
)
@bot.event
async def on_ready():
  await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="the time go by"))
karma = 100
print(f'karma = {karma}')
@bot.event
async def on_guild_join(guild):
  await guild.channel.send(f'Welcome, new Master!')
  await bot.process_commands(guild)
# settings
@bot.command()
async def command(ctx, *, arg = None):
  if arg == None:
    await ctx.send("uh you gotta give me the arg")
  else:
    await ctx.send(f"I'll go {arg}!")
ping = 0
@bot.command()
async def set(ctx, setting, of):
  global ping
  if setting == ("ping"):
    if of == ("on"):
      await ctx.send("ping is on")
      ping = 1
    else:
      await ctx.send("ping is off")
      ping = 0
  return
# create/delete
@bot.command()
async def cook(ctx, *, food):
  await ctx.send("I can try..")
  foodList = [f"Oh gosh\nUmm.. I think the {food} might need to wait for now..", f"It's perfect! {food} coming right up!", f"Ooh, ah, here's your {food}.."]
  time.sleep(1)
  await ctx.send(f"{choice(foodList, None, p=[0.67, 0.13, 0.20])}")
@bot.command()
async def make(ctx,*, name):
  guild = ctx.message.guild
  await guild.create_text_channel(name)
  await ctx.send(f"I made a new channel!")
@bot.command()
async def delete(ctx, *, channel_name):
  guild = ctx.message.guild
  existing_channel = discord.utils.get(guild.channels, name=channel_name)
  if existing_channel is not None:
    await existing_channel.delete(reason="None")
  else:
    await ctx.send(f'No {channel_name}')
#time
@bot.command()
async def planer(ctx, listnam, *, sched):
  weo = sched.replace(",".join(sched), "\n")
  embed=discord.Embed(title=f"{listnam}", description=f"{weo}", color=0xF0F0F0)
  await ctx.send(embed=embed)
@bot.command()
async def alarm(ctx, thyme=None, *, reminder=None):
  user = ctx.message.author
  if reminder == None:
    await ctx.send("No alarm name..? I'll set it anyhoo,")
    reminder = "your alarm"
  if thyme == None:
    await ctx.send('Oh, uh, I need a time for this to work..')
    return
  if thyme.endswith("d"):
    thyme = int(thyme[:-1])
    await ctx.send(f"Alrighty! I'll remind you in {thyme} days!")
    for i in range(thyme * 60 * 60 * 24):
      await asyncio.sleep(1)
  elif thyme.endswith("h"):
    thyme = int(thyme[:-1])
    await ctx.send(f"Okie dokie! I'll remind you in {thyme} hours!")
    for i in range(thyme * 60 * 60):
      await asyncio.sleep(1)
  elif thyme.endswith("m"):
    thyme = int(thyme[:-1])
    await ctx.send(f"Okay! I'll remind you in {thyme} minutes!")
    for i in range(thyme * 60):
      await asyncio.sleep(1)
  elif thyme.endswith("s"):
    thyme = int(thyme[:-1])
    await ctx.send(f"I'll remind you in {thyme} seconds!")
    for i in range(thyme):
      await asyncio.sleep(1)
    if ping == 1:
      await ctx.send(f"Alright {user.mention}, time for {reminder}!")
    else:
      await ctx.send(f"Alright, time for {reminder}!")
      return
#vc
@bot.event
async def on_message(message):
    await bot.process_commands(message)
    if message.author == bot.user:
        return
    if 'hello' in message.content:
        await message.channel.send('Hello there! :wave:')
bot.run('bees')

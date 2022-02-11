# Import Discord Packages
from email import message
from http import client
from multiprocessing.connection import Client
from turtle import title
import discord
from discord.ext import commands


client = commands.Bot(command_prefix='?')

@client.command()
async def Ping(context):
    
    await context.send('Pong!')
    
  
@client.command()
async def clearchat(context):
    
    await context.message.channel.send('What is the version!')   
    
    
@client.command(name='Version')
async def version(context):
    
    
    myEmbed = discord.Embed(title="Current Version", description="The bot is in version 1.0", color=0xff00)
    myEmbed.add_field(name="Version Code:", value="v1.0.0", inline=False)
    myEmbed.add_field(name="Date Released:", value="June 18th, 2020", inline=False)
    myEmbed.set_footer(text="This a sample footer")
    myEmbed.set_author(name="RiyaVasu Tyagi")
     
    await context.message.channel.send(embed=myEmbed)  
    
@client.event
async def on_ready():
    
    general_channel = client.get_channel(941448704655761418)
    await general_channel.send('Hello, world!')

@client.event
async def on_message(message):
    
    if message.content == 'Quote':
      general_channel = client.get_channel(941448704655761418)
      
      
      myEmbed = discord.Embed(title="Love the way you like", description="Sunny Day", color=0xff00)
      myEmbed.add_field(name="Version Code:", value="3.1.2", inline=False)
      myEmbed.add_field(name="Date Released:", value="June 18th, 2021", inline=False)
      myEmbed.set_footer(text="This a sample footer")
      myEmbed.set_author(name="RiyaVasu Tyagi")
      
      
      await general_channel.send(embed=myEmbed)  
    
      
    
 
# Run the client on the server
client.run('OTQxNDI5ODIxNzk4NDgxOTMy.YgV02A.8Bee5LXj6LaSZeubD0bwxK7mIXY')

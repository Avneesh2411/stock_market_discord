import os
import discord
from dotenv import load_dotenv
from discord.ext import commands

from stock_info import get_stock_info
from stock_recommendation import recommend_stocks
from utils import process_message

load_dotenv()
TOKEN = os.getenv('TOKEN')

bot = commands.Bot(command_prefix='!')

@bot.command(name='stock_info', help='Provides information about a specific stock')
async def stock_info(ctx, company_name: str):
    response = get_stock_info(company_name)
    await ctx.send(response)

@bot.command(name='recommend', help='Recommends stocks to buy')
async def recommend(ctx):
    recommendations = recommend_stocks()
    await ctx.send(recommendations)

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    msg = process_message(message.content)
    if msg:
        await message.channel.send(msg)

bot.run(TOKEN)
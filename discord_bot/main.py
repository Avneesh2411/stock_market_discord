import discord
from discord.ext import commands
import asyncio
from config import BOT_TOKEN
from commands.fetch_stock import fetch_stock
from commands.recommend_stock import recommend_stock
from utils.message_processing import process_message
from utils.error_handling import handle_error

class StockBot(commands.Bot):
    def __init__(self, command_prefix, self_bot):
        commands.Bot.__init__(self, command_prefix=command_prefix, self_bot=self_bot)

    async def on_ready(self):
        print(f'We have logged in as {self.user}')

    async def on_message(self, message):
        if message.author == self.user:
            return

        try:
            command, args = process_message(message.content)
            if command == 'fetch_stock':
                await fetch_stock(args)
            elif command == 'recommend_stock':
                await recommend_stock(args)
        except Exception as e:
            await handle_error(e, message.channel)

    async def on_error(self, event, *args, **kwargs):
        await handle_error(event, args, kwargs)

if __name__ == "__main__":
    bot = StockBot(command_prefix="!", self_bot=False)
    bot.run(BOT_TOKEN)
```python
import discord
from discord.ext import commands
from discord_bot.stock_api import get_stock_data
from discord_bot.utils.error_handling import handle_error
from discord_bot.utils.message_processing import process_message

class FetchStock(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='fetchstock', help='Fetches stock market details. Usage: !fetchstock <stock_symbol>')
    async def fetch_stock(self, ctx, *, message):
        try:
            stock_symbol = process_message(message)
            stock_data = get_stock_data(stock_symbol)
            await ctx.send(stock_data)
        except Exception as e:
            handle_error(e)

def setup(bot):
    bot.add_cog(FetchStock(bot))
```
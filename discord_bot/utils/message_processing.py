```python
import discord
from discord_bot.models.user_model import User

def process_message(message: discord.Message) -> User:
    """
    Process a message from a user and return a User object.
    """
    user_id = message.author.id
    user_name = message.author.name
    content = message.content

    return User(user_id, user_name, content)

def get_command_from_message(message: discord.Message) -> str:
    """
    Extract the command from the message content.
    """
    content = message.content
    command = content.split()[0]

    return command

def get_args_from_message(message: discord.Message) -> list:
    """
    Extract the arguments from the message content.
    """
    content = message.content
    args = content.split()[1:]

    return args
```
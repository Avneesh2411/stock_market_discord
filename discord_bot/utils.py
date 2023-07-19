def process_message(message):
    """
    Function to process the user's message and extract the command and arguments.
    """
    command = None
    args = None

    if message.startswith('!'):
        parts = message[1:].split(' ')
        command = parts[0]
        args = parts[1:]

    return command, args
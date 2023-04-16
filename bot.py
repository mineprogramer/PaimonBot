from dotenv import load_dotenv
import discord
import responses
import os

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

TOKEN = os.getenv("TOKEN")

async def send_message(message, user_message, is_private):
    try:
        response = responses.handle_response(user_message, message)
        if is_private == False :
            await message.channel.send(response)
        else :
            await message.author.send(response)
    except Exception as e:
        print(e)

def run_discord_bot():

    curses = {'fuck', 'shit', 'fucking'}
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is running!')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        
        user_message = str(message.content)
        channel = str(message.channel)

        if user_message[0] == '$':
            user_message = user_message[1:].lower()
            if user_message.startswith('say'):
                await message.channel.purge(limit = 1)
                await message.channel.send(message.content[4:])
            elif user_message == '$emoji' :
                await send_message(message, user_message, is_private=True)
            else :
                await send_message(message, user_message, is_private=False)
            
        if ('t' in user_message or 'T' in user_message) and user_message.len() >= 5:
            user_message = user_message.lower()
            t_index = user_message.find('t')
            if (user_message[t_index + 1] != 'e' and user_message[t_index + 2] == 'd' and
            user_message[t_index + 3] == 'd' and user_message[t_index + 4] == 'y') :
                await message.channel.send("Do you mean Teddy?")
            else:
                return
            
        if user_message in curses:
            await message.channel.send("HEYY WATCH YOUR LANGUAGE!")

    client.run(TOKEN)
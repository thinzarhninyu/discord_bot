import discord
import responses
import os
from dotenv import load_dotenv

load_dotenv()   

def create_intents():
    intents = discord.Intents.default()
    return intents

async def send_message(message, user_message, is_private):
    try:
        response = responses.handle_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print (e)
        
def run_discord_bot():
    TOKEN = os.getenv('TOKEN') 
    intents = create_intents()
    client = discord.Client(intents = intents)
    
    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')
        
    @client.event
    async def on_message(message):
        
        print("on_message event triggered")

        if message.author == client.user:
            return
        
        print(f"Received message: '{message.content}'")
        
        if message.content.lower() == "test":
            await message.channel.send("Received 'test' message!")
        
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)
        
        print(f"{username} said: '{user_message}' ({channel})")
        
        if user_message.strip() and user_message[0] == '?':
            user_message = user_message[1:]
            await send_message(message, user_message, is_private=True)
        else:
            await send_message(message, user_message, is_private=False)
        
    client.run(TOKEN)
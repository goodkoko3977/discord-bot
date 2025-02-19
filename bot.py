import discord
import os

TOKEN = os.getenv("TOKEN")  # Railwayの環境変数からTOKENを取得

intents = discord.Intents.all()  # すべてのIntentを有効化
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

client.run(TOKEN)

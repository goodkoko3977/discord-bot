import discord

# ここにBotのトークンを入れる（あとで環境変数で設定するため一旦空にする）
TOKEN = ""

intents = discord.Intents.default()
intents.reactions = True
intents.guilds = True
intents.members = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

client.run(TOKEN)

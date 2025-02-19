import discord
from discord.ext import commands

TOKEN = "os.getenv("TOKEN")"  # 環境変数を使うなら os.getenv("TOKEN")
GUILD_ID = 1329477297056776292  # サーバーID
CHANNEL_ID = 1341806746296913971  # 監視するチャンネルID
TARGET_EMOJI = "1340948199325831189"  # 指定のリアクション絵文字

# レベル1〜5までのロールID（昇格順に並べる）
ROLE_LEVELS = [
   1341694931772899368,  # 例: 123456789012345678
   1341696717866926123,  # 例: 223456789012345678
   1341697912240996382,  # 例: 323456789012345678
   1341698761277046924,  # 例: 423456789012345678
  1341699713661141063,  # 例: 523456789012345678
]

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"1340948199325831189 Botが起動しました！ {bot.user}")

async def promote_member(member):
    """現在のロールを確認し、次のレベルのロールを付与"""
    guild = member.guild
    current_roles = {role.id for role in member.roles}

    for i in range(len(ROLE_LEVELS) - 1):
        if ROLE_LEVELS[i] in current_roles and ROLE_LEVELS[i + 1] not in current_roles:
            next_role = discord.utils.get(guild.roles, id=ROLE_LEVELS[i + 1])
            if next_role:
                await member.add_roles(next_role)
                print(f"1340948199325831189 {member} にロール {next_role.name} を付与しました！")
            break  # 1つずつしか進めない

@bot.event
async def on_raw_reaction_add(payload):
    """リアクションが追加されたとき"""
    if payload.channel_id != CHANNEL_ID:
        return
    if str(payload.emoji) != TARGET_EMOJI:
        return

    guild = bot.get_guild(GUILD_ID)
    member = guild.get_member(payload.user_id)

    if member is not None:
        await promote_member(member)  # ロールを1段階昇格

bot.run(TOKEN)

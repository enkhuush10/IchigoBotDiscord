import discord
from discord.ext import commands
import os  # <-- Required to read the environment variable

# !!! IMPORTANT: DO NOT PUT YOUR TOKEN HERE !!!
# The token will be set as an environment variable named 'DISCORD_BOT_TOKEN' on your hosting service.
BOT_TOKEN = os.getenv('DISCORD_BOT_TOKEN')
WELCOME_CHANNEL_ID = 1467680849972564081
WELCOME_IMAGE_URL = 'https://instasize.com/p/7a7b80d5a29375ef22be6fea01fc16533549c385c484449eea89cc663cc94ce5'

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

def create_welcome_embed(member_mention):
    """Returns a Discord Embed object containing the welcome message and image."""
    embed = discord.Embed(
        color=discord.Color.from_rgb(255, 182, 193)
    )
    embed.title = f"୨୧ ⌗ Welcome, {member_mention}! ・✦"
    
    # Channel IDs REPLACED with proper Discord mentions.
    # Format: <#CHANNEL_ID_HERE> becomes a clickable channel link.
    embed.description = """
⊹₊꒷︶︶꒷︶︶꒷꒦︶︶꒦‧₊˚⊹︰🌷🌸🌷

📜 **‧₊˚ Important Channels**
— Rules: <#CHANNEL_ID_FOR_RULES>          # Replace with your rules channel ID
— Introduction: <#1465189276592635968>   # Already your introduction channel
— Chat: <#1465189276592635966>           # Already your general chat
— Announcements: <#CHANNEL_ID_FOR_ANNOUNCEMENTS>  # Replace with your announcements channel ID

🌸 **‧₊˚ Our Community Spaces**
✧ — <#1465189276592635966>               # General chat again
✧ — <#CHANNEL_ID_FOR_HELP_DESK>          # Replace with your help desk channel ID
✧ — <#1465190857895313431>               # Your memories category channel
✧ — <#1465192505178853428>               # Your voice channels category

🐇 **‧₊˚ What We Offer**
• A friendly and safe community
• Fun events and games
• Helpful resources and support
• Creative spaces to share your work

✦ ₊꒷꒦︶︶︶ ୨୧ ︶︶︶꒷꒦ෆ
ʚ *Hope you like our server and have fun!*
୨୧ Feel at ease and enjoy your stay! ♡ˎˊ˗
"""
    
    embed.set_image(url=WELCOME_IMAGE_URL)
    return embed

@bot.event
async def on_ready():
    print(f'{bot.user} is online!')

@bot.event
async def on_member_join(member):
    welcome_channel = bot.get_channel(WELCOME_CHANNEL_ID)
    if welcome_channel is None:
        print(f"ERROR: Could not find the welcome channel.")
        return
    
    welcome_embed = create_welcome_embed(member.mention)
    await welcome_channel.send(embed=welcome_embed)

@bot.command(name='test')
@commands.has_permissions(manage_messages=True)
async def test_command(ctx):
    welcome_channel = bot.get_channel(WELCOME_CHANNEL_ID)
    if welcome_channel is None:
        await ctx.send("Error: Welcome channel not found.")
        return
    
    welcome_embed = create_welcome_embed(ctx.author.mention)
    await welcome_channel.send(embed=welcome_embed)
    await ctx.send(f"✅ Tested! Check {welcome_channel.mention} for the embed.")

# The bot runs using the token from the environment variable
bot.run(BOT_TOKEN)

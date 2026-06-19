import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

# Dòng này giúp bot vẫn đọc được file .env khi bạn chạy thử nghiệm ở máy máy tính cá nhân
load_dotenv()

# Cấu hình các quyền (Intents) cho bot
intents = discord.Intents.default()
intents.message_content = True  # Cho phép bot đọc nội dung tin nhắn

bot = commands.Bot(command_code="!", intents=intents)

@bot.event
async def on_ready():
    print(f"=========================================")
    print(f" Bot đã đăng nhập thành công: {bot.user.name}")
    print(f" Hiện đang chạy trực tuyến 24/7 trên Host!")
    print(f"=========================================")

@bot.command()
async def ping(ctx):
    await ctx.send(f"🏓 Pong! Độ trễ của bot là {round(bot.latency * 1000)}ms")

# BƯỚC QUAN TRỌNG: Lấy Token từ môi trường hệ thống
# Trên máy tính: Nó sẽ tìm trong file .env
# Trên Railway: Nó sẽ lấy từ mục "Variables" mà bạn nhập trên web
TOKEN = os.getenv("TOKEN")

if TOKEN:
    bot.run(TOKEN)
else:
    print("❌ LỖI: Không tìm thấy TOKEN bot. Hãy kiểm tra lại cấu hình Variables trên Railway!")
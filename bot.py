import os
import yaml
import asyncio
import discord
from discord.ext import commands

import worldgen as worldgen


class MMORPGBOT(commands.Bot):
    def __init__(self, command_prefix, intents):
        super().__init__(command_prefix=commands.when_mentioned_or(command_prefix), intents=intents)

        self.botConfig = None
        self.gameConfig = None
        self.token = None
        self.startupCogs = []
        self.rpgworld = worldgen.world



    def load_config(self, filepathb_config, filepath_gconfig):
        print(f"loading botconfiguration: {filepathb_config}")
        # load config
        with open(filepathb_config) as stream:
            try:
                self.botConfig = yaml.safe_load(stream)

                # token
                self.token = self.botConfig["TOKEN"]
                print(f"token: {self.token}")
                
                # autoload cogs
                self.startupCogs = self.botConfig["STARTUP_COGS"]
                print("loading cogs:")
                for c in self.startupCogs:
                    print(f" - {c}")
                    asyncio.run(self.load_extension(f"cog.{c}"))

            except yaml.YAMLError as exc:
                print(exc)


        with open(filepath_gconfig) as stream:
            try:
                self.gameConfig = yaml.safe_load(stream)

            except yaml.YAMLError as exc:
                print(exc)
        print("configuration loaded")
        

    def bot_run(self):
        print("starting bot")
        self.run(self.token)


    async def on_ready(self):
        print(f'Connection to Discord established!')
        print(f'Username: {bot.user}')
        print(f'Connected Guilds: {len(bot.guilds)}')
        for guild in bot.guilds:
            print(f' - {guild.id}: {guild.name}')

        print("Ready")



bot = MMORPGBOT(command_prefix='<', intents=discord.Intents.default())
bot.load_config("config/botconfig.yaml", "config/gameconfig.yaml")
bot.bot_run()
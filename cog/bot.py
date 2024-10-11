import os
import discord
from discord.ext import commands



class Bot(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    async def cog_command_error(self, ctx, error):
        print(error)
        await ctx.send(error)


    @commands.command(name="ping")
    async def cmd_ping(self, ctx):
        """ ping pong command for bot response test"""
        await ctx.send("pong")


    @commands.group(name="cog", invoke_without_command=True)
    async def cmd_cog(self, ctx):
        """ controll of loaded cogs"""
        await ctx.send("Pls specify your action further ...")


    @cmd_cog.command(name="list")
    async def cmd_cog_list(self, ctx):
        """ lits all loaded cogs"""

        embed=discord.Embed(title="Cogs:", description="List of all loaded and available cogs")
        
        text = ""
        for cog in self.bot.cogs:
            text += f"- {cog} \n"
        embed.add_field(name="Loaded Cogs:", value=text, inline=True)

        text = ""
        for e in os.listdir("cog"):
            if not os.path.isfile(f"cog/{e}"): continue
            text += f"- {e}\n"
        embed.add_field(name="Available Extensions:", value=text, inline=True)

        await ctx.send(embed=embed)


    @cmd_cog.command(name="load")
    async def cmd_cog_load(self, ctx, cog:str):
        """ loads the specified cog"""
        print(f"loading cog: {cog}")
        await ctx.send(f"loading cog: {cog}")
        await self.bot.load_extension(f"cog.{cog}")


    @cmd_cog.command(name="unload")
    async def cmd_cog_unload(self, ctx, cog:str):
        """ unloads the specified cog"""
        print(f"unloading cog: {cog}")
        await ctx.send(f"unloading cog: {cog}")
        await self.bot.unload_extension(f"cog.{cog}")


    @cmd_cog.command(name="reload")
    async def cmd_cog_reload(self, ctx, cog:str):
        """ reloads the specified cog"""
        print(f"reloading cog: {cog}")
        await ctx.send(f"reloading cog: {cog}")

        await self.bot.unload_extension(f"cog.{cog}")
        await self.bot.load_extension(f"cog.{cog}")


async def setup(bot):
   await bot.add_cog(Bot(bot))
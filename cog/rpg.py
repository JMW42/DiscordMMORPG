"""  
# AUTHOR: JMW
# CREATION DATE: 04.10.2024
# LAST UPDATE: 12.10.2024
The RPG cog is responsible for the interaction between players and the game.
"""


import discord
from discord.ext import commands


from rpg import rpgcharacter as rpgcharacter
from rpg import rpgplayercharacter as pcharacter
from rpg import rpgstage as rpgstage
from rpg import rpgstageconnector as rpgstageconnectorgit 


async def is_loged_in(ctx):
        return ctx.author.id in ctx.bot.rpgworld.playercharacters



class RPG(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    

    async def cog_command_error(self, ctx, error):
        print(error)
        await ctx.send(error)
    

    @commands.command(name="check")
    async def cmd_check(self, ctx):
        """ test command"""
        await ctx.send(f"check: {ctx.author.id}")


    @commands.command(name="login")
    async def cmd_login(self, ctx):
        """ starts the login sequence for a player. This command needs to be run to participate in the game."""

        if not ctx.author.id in ctx.bot.rpgworld.playercharacters:
            
            # display welcome message
            await ctx.send(self.bot.gameConfig["WELCOMEMSG"])

            # cherate new player character
            char = pcharacter.RPGPlayerCharacter("pchar_player", str(ctx.author).replace(" ", ""), "a player character", self.bot.rpgworld.spawn_stage, ctx.author)
            
            # add player id to world list
            self.bot.rpgworld.playercharacters[ctx.author.id] = char

            # call character and stage command
            await self.cmd_character(ctx)
            await self.cmd_stage(ctx)

        else:
            await ctx.send("you need to be loged out to login!")
    


    @commands.command(name="character")
    @commands.check(is_loged_in)
    async def cmd_character(self, ctx):
        """ displays character information"""

        # get player character
        char = self.bot.rpgworld.playercharacters[ctx.author.id]

        # create embed and add values
        embed = discord.Embed(title=f"Character: {char.name} - {ctx.author.id}", description="Information about your ingame character")

        # player name
        embed.add_field(name="Name:", value=char.name, inline=True)

        # current stage
        embed.add_field(name="Stage:", value=char.stage.name, inline=True)

        # inventory:
        text = f"Total: {len(char.inventory.getItems())} items \n"
        for i in range(len(char.inventory.getItems())):
            item = char.inventory.getItems()[i]
            text += f" - [{i}] {item.name}\n"
        embed.add_field(name="Inventory:", value=text, inline=False)

        await ctx.send(embed=embed)


    @commands.command(name="stage")
    @commands.check(is_loged_in)
    async def cmd_stage(self, ctx):
        """ displays information about your current stage"""
        char = self.bot.rpgworld.playercharacters[ctx.author.id]
        embed = discord.Embed(title=f"Stage: {char.stage.name}", description=char.stage.description)
        
        # characters:
        text = ""
        for i in range(len(char.stage.characters)):
            text += f"- [{i}] {char.stage.characters[i].name}\n"
        embed.add_field(name="Characters:", value=text, inline=False)
        

        # objects:
        text = ""
        for i in range(len(char.stage.objects)):
            text += f"- [{i}] {char.stage.objects[i].name}\n"
        embed.add_field(name="Objects:", value=text, inline=False)


        # gates:
        text = ""
        for i in range(len(char.stage.connectors)):
            text += f"- [{i}] {char.stage.connectors[i].name}\n"
        embed.add_field(name="Gates:", value=text, inline=False)

        await ctx.send(embed=embed)


    @commands.command(name="travel")
    @commands.check(is_loged_in)
    async def cmd_travel(self, ctx, num:int, *args):
        """ allows a character to use a gate in his current stage and travel"""
        char = self.bot.rpgworld.playercharacters[ctx.author.id]

        if num < len(char.stage.connectors) and num >= 0:

            stage_old = char.stage
            g = stage_old.connectors[num]
            await g.travel(ctx, char, *args)

        else:
            await ctx.send(f"Pls enter a valid gate id!")


    @commands.command(name="inspect")
    @commands.check(is_loged_in)
    async def cmd_inspect(self, ctx, type:str, num:int, *args):
        """ inspects an entity from the secified group (object, gate, character, inventory) in your current stage or inventory"""
        char = self.bot.rpgworld.playercharacters[ctx.author.id]
        
        if type == "object":
            arr = char.stage.objects
        elif type == "inventory":
            arr = char.inventory.getItems()
        elif type == "connection":
            arr = char.stage.connectors
        elif type == "character":
            arr = char.stage.characters
        else:
            arr = []
        
        
        if num < len(arr) and num >= 0:
            obj = arr[num]
            
            embed = discord.Embed(title=f"Inspect: {obj.name}", description=obj.description)

            # type:
            embed.add_field(name="Type:", value=obj.__class__.__name__, inline=False)
            
            # stage:
            #embed.add_field(name="Stage:", value=obj.stage.name, inline=True)

            # dialoge:
            if hasattr(obj, "dialoge"):
                text = ""
                for msg in obj.dialoge:
                    text += f" - _{msg}_ \n"
                embed.add_field(name="Dialoge Options:", value=text, inline=False)


            #inspect(self, ctx, author, *args)
            await obj.inspect(ctx, char, *args)
            await ctx.send(embed=embed)
        else:
            await ctx.send(f"Pls enter a valid object id and type!")


    
    @commands.command(name="msg")
    @commands.check(is_loged_in)
    async def cmd_msg(self, ctx, msg:str):
        """ sends the specified message to all characters within your current stage e.g: msg "hello there". """
        char = self.bot.rpgworld.playercharacters[ctx.author.id]

        await ctx.send(f'{char.name} says: _"{msg}"_')

        await char.stage.sendMessageToAllCharacters(char, msg)
        

    @commands.command(name="interact")
    @commands.check(is_loged_in)
    async def cmd_interact(self, ctx, num:int, *args):
        """ interaction with a object in your current stage specified by num with given optional args: eg.: <interact 0 arg1 arg2 arg3 ... """
        char = self.bot.rpgworld.playercharacters[ctx.author.id]
        

        if num < len(char.stage.objects) and num >= 0:
            obj = char.stage.objects[num]
            await ctx.send(f"_{char.name}_ interacts with _{obj.name}_")
            await obj.interact(ctx, char, *args)
        else:
            await ctx.send(f"Pls enter a valid object id and type!")


async def setup(bot):
   await bot.add_cog(RPG(bot))
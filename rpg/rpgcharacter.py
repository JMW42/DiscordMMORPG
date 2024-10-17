"""  
# AUTHOR: JMW
# CREATION DATE: 04.10.2024
# LAST UPDATE: 13.10.2024
The RPGCharacter class is the base class for all further living beeings inside the RPG game.
"""


from rpg.rpgstage import RPGStage as RPGStage
from rpg.rpgstageentity import RPGStageEntity as RPGStageEntity

from rpg.rpginventory import RPGInventory as RPGInventory

class RPGCharacter (RPGStageEntity):
    def __init__(self, tag:str, name:str, description:str, stage:RPGStage=None, hasitem=True):
        super().__init__(tag, name, description, stage)
        
        if hasitem:
            self.inventory = RPGInventory()
        else:
            self.inventory = None 


        if not stage is None:
            stage.addRPGCharacter(self)
    
    
    async def inspect(self, ctx, author, *args):
        """ game method: will be called when the object is inspected. """
        await self.log(f"You are inspected by {author.name}")


    async def log(self, msg):
        """ The log method is called, whenever somehow an action is performed that is related to this character. """
        print(f'<{self.name}>: {msg}')


    async def recieveMessage(self, author, msg:str):
        """ This method is called whenever a character recieves a message by other characters, the game or annything else."""
        if not author is self: 
            await self.log(f'You hear _{author.name}_ saying: _"{msg}"_')
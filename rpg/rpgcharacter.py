"""  
# AUTHOR: JMW
# CREATION DATE: 04.10.2024
# LAST UPDATE: 13.10.2024
The RPGCharacter class is the base class for all further living beeings inside the RPG game.
"""


from rpg.rpgstage import RPGStage as RPGStage
from rpg.rpgstageentity import RPGStageEntity as RPGStageEntity


class RPGCharacter (RPGStageEntity):
    def __init__(self, tag:str, name:str, description:str, stage:RPGStage=None):
        super().__init__(tag, name, description, stage)
        self.inventory = []

        if not stage is None:
            stage.addRPGCharacter(self)
    
    
    async def inspect(self, ctx, author, *args):
        """ game method: will be called when the object is inspected. """
        pass


    async def log(self, msg):
        """ The log method is called, whenever somehow an action is performed that is related to this character. """
        print(f'<{self.name}>: {msg}')

    
    def hasRPGItemByTag(self, tag):
        """ Will return True if an item with an identical tag is found within the characters inventory, otherwise False is returned"""
        for item in self.inventory:
            if item.tag == tag: return True
        
        return False
    
    
    async def addRPGItemToInventory(self, item):
        """ This method adds the specified item to the characters inventory. """
        self.inventory.append(item)
        await self.log(f"You recieve item: _{item.name}_")
    

    async def removeRPGItemFromInventoryByTag(self, tag):
        """ This method removes the item specified by the given tag from the characters inventory. Will return the item on success and None otherwise."""

        for item in self.inventory:
            if item.tag == tag:
                self.inventory.remove(item)
                return item
        
        return None


    async def recieveMessage(self, author, msg:str):
        """ This method is called whenever a character recieves a message by other characters, the game or annything else."""
        if not author is self: 
            await self.log(f'You hear _{author.name}_ saying: _"{msg}"_')
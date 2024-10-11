"""  
# AUTHOR: JMW
# CREATION DATE: 04.10.2024
# LAST UPDATE: 11.10.2024
The RPGCharacter class is the base class for all further living beeings inside the RPG game.
"""


from rpg.rpgstage import RPGStage as RPGStage
from rpg.rpgentity import RPGEntity as RPGEntity


class RPGCharacter (RPGEntity):
    def __init__(self, tag:str, name:str, description:str, stage:RPGStage=None):
        super().__init__(tag, name, description)
        self.inventory = []

        if not stage is None:
            stage.add_character(self)
    
    
    async def inspect(self, ctx, author, *args):
        pass


    async def character_log(self, msg):
        print(f'CLOG <{self.name}>: {msg}')

    
    async def add_item(self, item):
        self.inventory.append(item)
        await self.character_log(f"_{self.name}_ recieves item: _{item.name}_")
    

    async def recieve_message(self, author, msg:str):
        if not author is self: 
            print(f"RCV: {author.name} -> {self.name}: {msg}")


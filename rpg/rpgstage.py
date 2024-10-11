"""  
# AUTHOR: JMW
# CREATION DATE: 04.10.2024
# LAST UPDATE: 04.10.2024
The RPGStage class is the base class for all game rooms/levels. Characters and objects are living in stages, gates allow to connect them via traveling.
"""

#from rpg.rpgworld import RPGWorld as RPGWorld
from rpg.rpgentity import RPGEntity as RPGEntity

class RPGStage(RPGEntity):
    def __init__(self, tag:str, name:str, description:str=None, world=None):
        super().__init__(tag, name, description)
        self.characters = []
        self.objects = []
        self.connectors = []
        self.world = world

        if not world is None:
            world.add_stage(self)

    
    def add_object(self, obj):
        self.objects.append(obj)
        obj.stage = self
    

    def add_character(self, character):
        self.characters.append(character)
        character.stage = self
    

    def remove_character(self, character):
        self.characters.remove(character)
        character.stage = None


    async def msg_to_characters(self, author, msg):
        for char in self.characters:
            await char.recieve_message(author, msg)
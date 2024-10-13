"""  
# AUTHOR: JMW
# CREATION DATE: 04.10.2024
# LAST UPDATE: 13.10.2024
The RPGStage class is the base class for all game rooms/levels. Characters and objects are living in stages, gates allow to connect them via traveling.
"""

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

    
    def addRPGStageObject(self, obj):
        """ Adds a RPGStageObject like object to the stage."""
        self.objects.append(obj)
        obj.stage = self
    

    def removeRPGStageObject(self, obj):
        """ Removes a RPGStageObject like object from the stage if it is on stage. Will return True in this case, otherwise False"""
        if obj in self.objects:
            self.objects.remove(obj)
            obj.stage = None
            return True
        else:
            return False
    

    def addRPGCharacter(self, char):
        """ Adds a RPGCharacter like object to the stage."""
        self.characters.append(char)
        char.stage = self
    

    def removeRPGCharacter(self, char):
        """ Removes a RPGCharacter like object from the stage if it is on stage. Will return True in this case, otherwise False"""
        if char in self.characters:
            self.characters.remove(char)
            char.stage = None
            return True
        else:
            return False


    async def sendMessageToAllCharacters(self, author, msg):
        """ Sends the specified message to all characters on this stage."""
        for char in self.characters:
            await char.recieveMessage(author, msg)
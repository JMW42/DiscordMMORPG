"""  
# AUTHOR: JMW
# CREATION DATE: 04.10.2024
# LAST UPDATE: 13.10.2024
The RPGPlayerCharacter class used for player characters.
"""

from rpg.rpgcharacter import RPGCharacter
from rpg.rpgstage import RPGStage as RPGStage
import asyncio


class RPGPlayerCharacter(RPGCharacter):
    def __init__(self, tag:str, name:str, description:str, stage:RPGStage, player):
        #self, name:str, description:str, stage:RPGStage
        super().__init__(tag, name, description, stage)
        self.player = player
    

    async def log(self, msg):
        """ inherited method from RPGCharacter. The log method is called, whenever somehow an action is performed that is related to this character. """
        print(f'_{self.name}_: {msg}')
        await self.player.send(f'_{self.name}_: {msg}')


    #async def recieveMessage(self, author, msg):
    #    """ inherited method from RPGCharacter. This method is called whenever a character recieves a message by other characters, the game or annything else."""
    #    if not author is self: 
    #        await self.character_log(f'You hear _{author.name}_ saying: _"{msg}"_')
    #        #await self.player.send(f'{author.name} says: _"{msg}"_')
        
    

from rpg.rpgcharacter import RPGCharacter
from rpg.rpgstage import RPGStage as RPGStage
import asyncio


class RPGPlayerCharacter(RPGCharacter):
    def __init__(self, tag:str, name:str, description:str, stage:RPGStage, player):
        #self, name:str, description:str, stage:RPGStage
        super().__init__(tag, name, description, stage)
        self.player = player
    

    async def character_log(self, msg):
        print(f'PLOG <{self.name}>: {msg}')
        await self.player.send(f'PLOG <{self.name}>: {msg}')


    async def recieve_message(self, author, msg):
        if not author is self: 
            print(f"RCV: {author.name} -> {self.name}: {msg}")
            await self.player.send(f'{author.name} says: _"{msg}"_')
        
    

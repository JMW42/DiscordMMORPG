"""  
# AUTHOR: JMW
# CREATION DATE: 04.10.2024
# LAST UPDATE: 13.10.2024
The RPGNonPlayerCharacter class is a NPC class that allows to create a character that is not controlled by a player and has the ability to talk.
"""



from rpg.rpgcharacter import RPGCharacter
from rpg.rpgstage import RPGStage as RPGStage
from difflib import SequenceMatcher
import asyncio
import yaml



class RPGDialogeNPC(RPGCharacter):
    def __init__(self, tag:str, name:str, description:str, stage:RPGStage=None, dialoge=None):
        super().__init__(tag, name, description, stage)
        self.dialoge=dialoge
         

    async def recieveMessage(self, author:RPGCharacter, msg:str):
        """ inherited method from RPGCharacter. This method is called whenever a character recieves a message by other characters, the game or annything else."""
        if not author is self: 
            await self.log(f'hears _{author.name}_ saying: _"{msg}"_')
            
            sim = []
            for key in self.dialoge:
                 sim.append(SequenceMatcher(None, str(key), str(msg)).ratio())
            
    	    
            if max(sim) > 0.85:
                index_max = max(range(len(sim)), key=sim.__getitem__)
                
                dopt = self.dialoge[list(self.dialoge.keys())[index_max]]

                check = True

                # take item
                if dopt["takeitem"] != None:
                    
                    if author.inventory.checkForItemByTag(dopt["takeitem"]):
                        author.inventory.removeItemByTag(dopt["takeitem"])
                    else:
                        check = False
                
                
                # dialoge response based on check
                if check:
                    await self.stage.sendMessageToAllCharacters(self, dopt["response"])
                else:
                    await self.stage.sendMessageToAllCharacters(self, dopt["failresp"])


                # give item
                if(dopt["giveitem"] != None):
                    item = loadRPGItem(dopt["giveitem"])
                    author.inventory.addItem(item)


from rpg.rpgloader import loadRPGItem as loadRPGItem
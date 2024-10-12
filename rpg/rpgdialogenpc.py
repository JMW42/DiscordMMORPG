"""  
# AUTHOR: JMW
# CREATION DATE: 04.10.2024
# LAST UPDATE: 12.10.2024
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

        print(dialoge)

    
    def load_character_config(self, filepath:str):
        with open(filepath) as stream:
            try:
                config = yaml.safe_load(stream)
                self.name = config["name"]
                self.description = config["description"]
                self.dialoge = config["dialoge"]
                return self
            except yaml.YAMLError as exc:
                print(exc)
         
         

    async def recieve_message(self, author, msg):
        """ this function is called when a npc recieves a message, from the given author.."""
        if not author is self: 
            await self.character_log(f'hears _{author.name}_ saying: _"{msg}"_')
            
            sim = []
            for key in self.dialoge:
                 sim.append(SequenceMatcher(None, str(key), str(msg)).ratio())
            

            if max(sim) > 0.75:
                index_max = max(range(len(sim)), key=sim.__getitem__)
                
                dopt = self.dialoge[list(self.dialoge.keys())[index_max]]

                check = True

                # take item
                if dopt["takeitem"] != None:
                    
                    if author.check_for_item_by_tag(dopt["takeitem"]):
                        await author.remove_item_by_tag(dopt["takeitem"])
                    else:
                        check = False
                
                
                # dialoge response based on check
                if check:
                    await self.stage.msg_to_characters(self, dopt["response"])
                else:
                    await self.stage.msg_to_characters(self, dopt["failresp"])


                # give item
                if(dopt["giveitem"] != None):
                    item = loadRPGItem(dopt["giveitem"])
                    await author.add_item(item)


from rpg.rpgloader import loadRPGItem as loadRPGItem
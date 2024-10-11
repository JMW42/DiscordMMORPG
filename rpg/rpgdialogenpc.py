"""  
# AUTHOR: JMW
# CREATION DATE: 04.10.2024
# LAST UPDATE: 11.10.2024
The RPGNonPlayerCharacter class is a NPC class that allows to create a character that is not controlled by a player and has the ability to talk.
"""

from rpg.rpgcharacter import RPGCharacter
from rpg.rpgstage import RPGStage as RPGStage
from difflib import SequenceMatcher
import asyncio
import yaml


class RPGDialogeNPC(RPGCharacter):
    def __init__(self, tag:str, name:str, description:str, stage:RPGStage=None, response=None):
        super().__init__(tag, name, description, stage)
        self.response=response

    
    def load_character_config(self, filepath:str):
        with open(filepath) as stream:
            try:
                config = yaml.safe_load(stream)
                self.name = config["name"]
                self.description = config["description"]
                self.response = config["response"]
                #npc = RPGNonPlayerCharacter(config["name"], config["description"], stage, config["response"])
                #return npc
                return self
            except yaml.YAMLError as exc:
                print(exc)
         
         

    async def recieve_message(self, author, msg):
        """ this function is called when a npc recieves a message, from the given author.."""
        if not author is self: 
            print(f"RCVNPC: {author.name} -> {self.name}: {msg}")
            
            sim = []
            for key in self.response:
                 sim.append(SequenceMatcher(None, str(key), str(msg)).ratio())
            

            if max(sim) > 0.75:
                index_max = max(range(len(sim)), key=sim.__getitem__)
                
                await self.stage.msg_to_characters(self, self.response[list(self.response.keys())[index_max]]) 

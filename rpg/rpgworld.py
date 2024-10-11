"""  
# AUTHOR: JMW
# CREATION DATE: 04.10.2024
# LAST UPDATE: 04.10.2024
The RPGWorld class is the base class for all worlds simulated by teh game. A Worlds main task is to manage the added stages and playercharacters.
"""

#from rpg.rpgstage import RPGStage as RPGStage
from rpg.rpgcharacter import RPGCharacter as RPGCharacter
from rpg.rpgplayercharacter import RPGPlayerCharacter as RPGPlayerCharacter
from rpg.rpgentity import RPGEntity as RPGEntity



class RPGWorld(RPGEntity):
    def __init__(self, tag:str, name:str, description:str):
        super().__init__(tag, name, description)

        self.playercharacters = {}
        self.stages = []
        self.spawn_stage = None
    

    def add_stage(self, stage):
        self.stages.append(stage)

    
    def add_playercharacter(self, pchar):
        self.playercharacters.append(pchar)
        self.spawn_stage.add_character(pchar)
"""  
# AUTHOR: JMW
# CREATION DATE: 13.10.2024
# LAST UPDATE: 13.10.2024
The RPGStageEntity class implements the ability of localizing an entity on a stage.
"""

from rpg.rpgentity import RPGEntity as RPGEntity
from rpg.rpgstage import RPGStage as RPGStage


class RPGStageEntity(RPGEntity):
    def __init__(self, tag:str, name:str, description:str, stage:RPGStage=None):
        super().__init__(tag, name, description)
        
        self.stage = stage

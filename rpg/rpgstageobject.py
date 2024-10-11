"""  
# AUTHOR: JMW
# CREATION DATE: 04.10.2024
# LAST UPDATE: 11.10.2024
The RPGStageObject class is the base class for all non living objects that are located in a stage that are no RPGGates.
"""

from rpg.rpgentity import RPGEntity as RPGEntity
from rpg.rpgstage import RPGStage as RPGStage

class RPGStageObject(RPGEntity):
    def __init__(self, tag:str, name:str, description:str, stage:RPGStage):
        super().__init__(tag, name, description)
        self.stage = stage
        
        if not stage is None:
            stage.add_object(self)


    async def inspect(self, ctx, author, *args):
        pass


    async def interact(self, ctx, author, *args):
        pass

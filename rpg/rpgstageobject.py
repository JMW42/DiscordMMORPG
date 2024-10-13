"""  
# AUTHOR: JMW
# CREATION DATE: 04.10.2024
# LAST UPDATE: 13.10.2024
The RPGStageObject class is the base class for all non living objects that are located in a stage that are no RPGGates.
"""

from rpg.rpgstageentity import RPGStageEntity as RPGStageEntity
from rpg.rpgstage import RPGStage as RPGStage

class RPGStageObject(RPGStageEntity):
    def __init__(self, tag:str, name:str, description:str, stage:RPGStage=None):
        super().__init__(tag, name, description, stage)
        
        if not stage is None:
            stage.addRPGStageObject(self)


    async def inspect(self, ctx, author, *args):
        """ game method: will be called when the object is inspected. """
        pass


    async def interact(self, ctx, author, *args):
        """ game method: will be called when the object is interacted with"""
        pass

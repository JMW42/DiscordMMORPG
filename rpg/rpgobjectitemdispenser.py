"""  
# AUTHOR: JMW
# CREATION DATE: 04.10.2024
# LAST UPDATE: 11.10.2024
The RPGStageObject class is the base class for all non living objects that are located in a stage that are no RPGGates.
"""

from rpg.rpgstageobject import RPGStageObject as RPGStageObject
from rpg.rpgentity import RPGEntity as RPGameEntity
from rpg.rpgstage import RPGStage as RPGStage

from rpg.rpgloader import loadRPGItem as loadRPGItem

import yaml


class RPGStageObjectItemDispenser(RPGStageObject):
    def __init__(self, tag:str, name:str, description:str, stage:RPGStage, filepath_item:str):
        super().__init__(tag, name, description, stage)
        self.filepath_item = filepath_item

    def inspect(self, author, *args):
        return


    async def interact(self, ctx, author, *args):
        item = loadRPGItem(self.filepath_item)
        await author.add_item(item)
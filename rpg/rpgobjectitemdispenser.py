"""  
# AUTHOR: JMW
# CREATION DATE: 04.10.2024
# LAST UPDATE: 04.10.2024
The RPGStageObject class is the base class for all non living objects that are located in a stage that are no RPGGates.
"""

from rpg.rpgstageobject import RPGStageObject as RPGStageObject
from rpg.rpgentity import RPGGameEntity as RPGameEntity
from rpg.rpgstage import RPGStage as RPGStage


from rpg.rpgitemkey import RPGItemKey as RPGItemKey


class RPGStageObjectItemDispenser(RPGStageObject):
    def __init__(self, tag:str, name:str, description:str, stage:RPGStage):
        super().__init__(tag, name, description, stage)
        self.tmp = 0

    def inspect(self, author, *args):
        return


    async def interact(self, ctx, author, *args):
        self.tmp += 1
        item = RPGItemKey("Rusty Iron Key" + str(self.tmp), "A rusty iron key, that might be allow to open rusty doors", 11221122)

        await ctx.send(f"_{author.name} interacts with {self.name} and finds an *{item.name}*_")
        await author.add_item(item)
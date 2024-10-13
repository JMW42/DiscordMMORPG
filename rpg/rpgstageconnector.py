"""  
# AUTHOR: JMW
# CREATION DATE: 04.10.2024
# LAST UPDATE: 13.10.2024
The RPGStageConnector allows characters to travel between stages.
"""

from rpg import rpgcharacter as rpgcharacter
from rpg import rpgstage as rpgstage
from rpg.rpgentity import RPGEntity as RPGEntity


class RPGStageConnector(RPGEntity):
    def __init__(self, tag:str, name:str, description:str, stage1, stage2):
        super().__init__(tag, name, description)
        self.stage1 = stage1
        self.stage2 = stage2

        self.stage1.connectors.append(self)
        self.stage2.connectors.append(self)
    

    async def inspect(self, ctx, author, *args):
        """ game method: will be called when the object is inspected. """
        pass


    async def travel(self, ctx, author, *args):
        """ game method: will be called when a character tries to travel to another stage by this connector. """

        # transport logic: where to go?
        if author.stage == self.stage1:
            # travel to stage 2
            stage_old = self.stage1
            stage_new = self.stage2

        else:
            # travel to stage 1
            stage_old = self.stage2
            stage_new = self.stage1

        # leave old stage:
        await author.log(f"You left: {stage_old.name}")
        stage_old.removeRPGCharacter(author)

        # enter new stage
        await author.log(f"You are entering: {stage_new.name}")
        stage_new.addRPGCharacter(author)
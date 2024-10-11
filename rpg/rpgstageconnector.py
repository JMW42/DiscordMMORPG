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
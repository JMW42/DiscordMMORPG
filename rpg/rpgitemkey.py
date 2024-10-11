"""  
# AUTHOR: JMW
# CREATION DATE: 04.10.2024
# LAST UPDATE: 04.10.2024
The RPGItemKey class is used for keys, that allow to open doors, chests, etc. ...
"""

from rpg.rpgitem import RPGItem as RPGItem
from rpg.rpgentity import RPGGameEntity as RPGameEntity



class RPGItemKey(RPGItem):
    def __init__(self, tag:str, name:str, description:str, keycode:int):
        super().__init__(tag, name, description)
        self.keycode = keycode

    def use_item(self, char):
        print(f"using {self.name} by {char.name}")

    

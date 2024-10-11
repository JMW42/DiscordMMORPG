"""  
# AUTHOR: JMW
# CREATION DATE: 04.10.2024
# LAST UPDATE: 04.10.2024
The RPGItem class is the base class for all Items inside the RPG game that can be stired in inventories or eqiped.
"""

from rpg.rpgentity import RPGEntity as RPGEntity
from dataclasses import dataclass


@dataclass
class RPGItem(RPGEntity):
    def __init__(self, tag:str, name:str, description:str):
        super().__init__(tag, name, description)
    

    def use_item(self, char):
        print(f"using {self.name} by {char.name}")
    

    
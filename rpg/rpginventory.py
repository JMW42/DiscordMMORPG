"""  
# AUTHOR: JMW
# CREATION DATE: 17.10.2024
# LAST UPDATE: 17.10.2024
The RPGInventory, the base class for item containers, implemented in characters, lootboxes, etc. ...
"""

#from rpg.rpgentity import RPGEntity as RPGEntity

from rpg.rpgitem import RPGItem as RPGItem
from typing import List

class RPGInventory:
    def __init__(self) -> None:
        self._inventory:List[RPGItem] = []


    def getItems(self):
        """ returns a list with the contained items"""
        return self._inventory


    def addItem(self, item:RPGItem):
        """ adds an item to the inventory, returns true on success"""
        self._inventory.append(item)
        return True


    def removeItem(self, item:RPGItem):
        """ tries to remove the specified item in the case it is inside the inventory. on success True is return otherwise False."""
        if item in self._inventory:
            self._inventory.remove(item)
            return True
        else: 
            return False


    def checkForItem(self, item:RPGItem):
        """ checks if the specified item is in the inventory.
        This"""
        return item in self._inventory
    
    
    def checkForItemByTag(self, tag:str):
        """ Checks if an item with a simillar tag is in the inventory."""
        for item in self._inventory:
            if item.tag == tag:
                return True
        
        return False
    

    def removeItemByTag(self, tag:str):
        """ Removes the first item found with the identical tag and returns true otherwise False is returned."""
        for item in self._inventory:
            if item.tag == tag:
                self._inventory.remove(item)
                return True
        
        return False
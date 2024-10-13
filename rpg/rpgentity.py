"""  
# AUTHOR: JMW
# CREATION DATE: 04.10.2024
# LAST UPDATE: 13.10.2024
The RPGGameEntity class is the base class for all further RPG class objects that are included in the game.
"""



class RPGEntity:
    def __init__(self, tag:str, name:str, description:str):
        self.tag = tag # identifier
        self.name = name # shown name ingame
        self.description = description # description text for the entity

        print(f"initialising entity: {self.tag}")


    def __str__(self):
        return self.name
    

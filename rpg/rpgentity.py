"""  
# AUTHOR: JMW
# CREATION DATE: 04.10.2024
# LAST UPDATE: 06.10.2024
The RPGGameEntity class is the base class for all further RPG class objects that are included in the game.
"""



class RPGEntity:
    def __init__(self, tag:str, name:str, description:str):
        self.tag = tag
        self.name = name
        self.description = description

        print(f"initialising entity: {self.tag}")


    def __str__(self):
        return self.name
    

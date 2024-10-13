"""  
# AUTHOR: JMW
# CREATION DATE: 08.10.2024
# LAST UPDATE: 12.10.2024
This files gives several usefull files for handling and loading rpg class objects.
"""

from rpg.rpgstageobject import RPGStageObject as RPGStageObject
from rpg.rpgentity import RPGEntity as RPGEntity
from rpg.rpgstage import RPGStage as RPGStage
from rpg.rpgstageconnector import RPGStageConnector as RPGStateConnector
from rpg.rpgdialogenpc import RPGDialogeNPC as RPGDialogeNPC
from rpg.rpgitem import RPGItem as RPGItem

import yaml


def loadRPGEntity(filepath=""):
    """ returns a RPGEntity instance with the properties specified in the given file by filepath. """
    with open(filepath) as stream:
        try:
            config = yaml.safe_load(stream)
            return RPGEntity(config["tag"], config["name"], config["description"])
        except yaml.YAMLError as exc:
            print(exc)
    


def loadRPGStage(filepath, world=None):
    """ returns a RPGStage instance with the properties specified in the given file by filepath. """
    #RPGStage("stage_lono_spawn", "Tavern Backyard", "spawn stage description", world)
    with open(filepath) as stream:
        try:
            config = yaml.safe_load(stream)
            return RPGStage(config["tag"], config["name"], config["description"], world)
        except yaml.YAMLError as exc:
            print(exc)


def loadRPGStageObject(filepath, stage=None):
    """ returns a RPGStageObject instance with the properties specified in the given file by filepath. """
    #RPGStageObject("object_garbage_pile", "Pile of Garbage", "A pile of garbage someone left here.", stage_tavern_backyard)
    with open(filepath) as stream:
        try:
            config = yaml.safe_load(stream)
            return RPGStageObject(config["tag"], config["name"], config["description"], stage)
        except yaml.YAMLError as exc:
            print(exc)


def loadRPGStateConnector(filepath, stage1=None, stage2=None):
    """ returns a RPGStageConnector instance with the properties specified in the given file by filepath. """
    with open(filepath) as stream:
        try:
            config = yaml.safe_load(stream)
            return RPGStateConnector(config["tag"], config["name"], config["description"], stage1, stage2)
        except yaml.YAMLError as exc:
            print(exc)



def loadRPGDialogeNPC(filepath, stage=None):
    """ returns a RPGDialogeNPC instance with the properties specified in the given file by filepath. """
    with open(filepath) as stream:
        try:
            config = yaml.safe_load(stream)
            return RPGDialogeNPC(config["tag"], config["name"], config["description"], stage, dialoge=config["dialoge"])
        except yaml.YAMLError as exc:
            print(exc)


def loadRPGItem(filepath, stage=None):
    """ returns a RPGItem instance with the properties specified in the given file by filepath. """
    with open(filepath) as stream:
        try:
            config = yaml.safe_load(stream)
            itype = filepath.split("_")[0]

            if itype == "item":
                # tag:str, name:str, description:str
                return RPGItem(config["tag"], config["name"], config["description"])
            else:
                return RPGItem(config["tag"], config["name"], config["description"])
                print(f"ERROR LOADING ITEM: {filepath}")
        except yaml.YAMLError as exc:
            print(exc)
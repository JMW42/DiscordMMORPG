"""  
# AUTHOR: JMW
# CREATION DATE: 06.10.2024
# LAST UPDATE: 06.10.2024
Testcode for creating a world based on its classes.
"""

from rpg.rpgworld import RPGWorld as RPGWorld
from rpg.rpgstage import RPGStage as RPGStage
from rpg.rpgstageobject import RPGStageObject as RPGStageObject
from rpg.rpgstageconnector import RPGStageConnector as RPGStageConnector
from rpg.rpgdialogenpc import RPGDialogeNPC as RPGDialogeNPC
from rpg.rpgobjectitemdispenser import RPGStageObjectItemDispenser as RPGStageObjectItemDispenser

from rpg.rpgloader import *


# WORLD:
world = RPGWorld("world_queensshore", "Riverside", "A small and piecfull district in the northern republic. Manny legendary adventures originate from this place.")


# STAGE: TAVERN BSACKYARD
stage_tavern_backyard = loadRPGStage("assets/stage_lono_tavern_backyard.yaml", world)
world.spawn_stage = stage_tavern_backyard


loadRPGStageObject("assets/object_wooden_crates.yaml", stage_tavern_backyard)
loadRPGStageObject("assets/object_garbage_pile.yaml", stage_tavern_backyard)
RPGStageObjectItemDispenser("object_disp_testitem", "Create of Testitems", "This create supplies you with test items", stage_tavern_backyard, "assets/items/item_testitem.yaml")
loadRPGDialogeNPC("assets/dnpc_lono_old_man.yaml", stage=stage_tavern_backyard)


# STAGE: TAVERN BARROOM
stage_tavern_bar = loadRPGStage("assets/stage_lono_tavern.yaml", world)


loadRPGStateConnector("assets/connector_lono_tavern.yaml", stage_tavern_backyard, stage_tavern_bar)
#RPGStageConnector("connector_lono_tavern", "Backyard door", "The backyard door of the The Bronze Lantern Tavern.", stage_tavern_backyard, stage_tavern_bar)


# STAGE: MARKET SQUARE
market_square = loadRPGStage("assets/stage_lono_market_square.yaml", world)

loadRPGStateConnector("assets/connector_lono_tavern_market.yaml", stage_tavern_backyard, market_square)
#RPGStageConnector("connector_lono_tavern_market", "Wooden fence gate", "This wooden fence gate leads you to the market place.", stage_tavern_backyard, market_square)

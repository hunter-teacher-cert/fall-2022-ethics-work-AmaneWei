import compatibility_checker

import pokemon_driver
from pokemon import Player, Pokemon, Move, INVALID_MOVE, INVALID_POKEMON

# --------------------------------------------
# razor_leaf = Move("Razor Leaf", 20, "grass")

# waterMon = Pokemon("WaterMon", 100, [], "water", 10)

# g_against_w = razor_leaf.get_multiplier_against(waterMon)
# print("The multipler from grass to water is", g_against_w)

# -----------------------------------------------

ember = Move("Ember", 20, "fire")
flame = Move("Flamethrower", 40, "fire")
bubble = Move("Bubble", 20, "water")
earthquake = Move("Earthquake", 40, "ground")
thunder = Move("Thunder Shock", 30, "electric")

charmander = Pokemon("Charmander", 100, [ember, flame], "fire", 50)
onix = Pokemon("Onix", 100, [earthquake], "ground", 40)
party1 = [charmander, onix]

pikachu = Pokemon("Pikachu", 100, [thunder], "electric", 80) 
squirtle = Pokemon("Squirtle", 100, [bubble], "water", 50)
party2 = [pikachu, squirtle]

p1 = Player("Kevin", party1)
p2 = Player("Ryan", party2)

pokemon_driver.main(p1, p2)

import random

'''
Plan: Have the students make a pokemon class and make their own pokemon + team
We will probably give them starting code, the way that TEALS had it 

We will create the driver and move class
Have a pokemon battle at the last couple days of school?
'''

# https://meet.google.com/ptq-nhbd-cjh

"""
Rules:
Give a range of HP??? Cannot exceed 255?

"""


class Player:
    def __init__(self, name, pokemon_party):
        self.name = name
        self.pokemon_party = pokemon_party
        self.current_pokemon = pokemon_party[0]

    def list_pokemon(self):
        for pokemon in self.pokemon_party:
            if not pokemon.is_alive():
                print(pokemon.name + " (fainted)")
            elif pokemon == self.current_pokemon:
                print(pokemon.name + " (current)")
            else:
                print(pokemon.name)

    def switch(self, pokemon_name):
        new_pokemon = self.get_pokemon(pokemon_name)
        if new_pokemon == INVALID_POKEMON:
            return False

        if not new_pokemon.is_alive():
            return False

        if new_pokemon == self.current_pokemon:
            return False
            
        self.current_pokemon = new_pokemon
        return True
        
    def get_pokemon(self, pokemon_name):
        for pokemon in self.pokemon_party:
            if pokemon.name.lower() == pokemon_name.lower():
                return pokemon

        return INVALID_POKEMON
    
    def heal(self):
        self.current_pokemon.heal()

    def team_is_alive(self):
        for pokemon in self.pokemon_party:
            if pokemon.is_alive():
                return True

        return False

    def print_moves(self):
        """Prints every move name in the current pokemon's moveset"""
        for move in self.current_pokemon.moves:
            print(move)

    def attack(self, move_name, enemy_pokemon):
        self.current_pokemon.attack(move_name, enemy_pokemon)


class Pokemon:
    def __init__(self, name, hp, moves, type, speed):
        """
        name: string representing p's name
        
        """
        
        self.hp = hp
        self.max_hp = hp
        self.name = name
        self.moves = moves
        self.type = type
        self.speed = speed

    def is_alive(self):
        return self.hp > 0

    # arrow for function
    # colon for variables
    def print_moves(self) -> int:
        for move in self.moves:
            print(move)

    def get_move(self, move_name: str):
        for move in self.moves:
            if move.name.lower() == move_name.lower():
                return move
                
        return INVALID_MOVE

    def attack(self, move_name, enemy):
        move = self.get_move(move_name)
        damage = move.power * move.get_multiplier_against(enemy)
        enemy.take_damage(damage)

    def take_damage(self, damage_amount):
        self.hp -= damage_amount
        if self.hp < 0: 
            self.hp = 0
        self.hp = int(self.hp)
        
    def heal(self):
        self.hp += 20
        if self.hp > self.max_hp:
            self.hp = self.max_hp


class Move:
    def __init__(self, name, power, type):
        self.name = name
        self.power = power
        self.type = type

    def __str__(self):
        return self.name + ": " + self.type + " type"

    def get_multiplier_against(self, pokemon):
        """
        https://bulbapedia.bulbagarden.net/wiki/Type/Type_chart#Generation_I
        """

        if self.type == "grass":
            if pokemon.type == "water" or pokemon.type == "ground":
                return 2
            elif pokemon.type == "fire" or pokemon.type == "grass":
                return 0.5
            else:
                return 1
                
        elif self.type == "fire":
            if pokemon.type == "grass":
                return 2
            elif pokemon.type == "water" or pokemon.type == "fire":
                return 0.5
            else:
                return 1
                
        elif self.type == "water":
            if pokemon.type == "fire" or pokemon.type == "ground":
                return 2
            elif pokemon.type == "grass" or pokemon.type == "water":
                return 0.5
            else:
                return 1
                
        elif self.type == "ground": 
            if pokemon.type == "fire" or pokemon.type == "electric":
                return 2
            elif pokemon.type == "grass":
                return 0.5
            else:
                return 1
            
        elif self.type == "electric": 
            if pokemon.type == "water":
                return 2
            elif pokemon.type == "grass" or pokemon.type == "electric":
                return 0.5
            elif pokemon.type == "ground":
                return 0
            else:
                return 1
            
        else:
            return 1


INVALID_MOVE = Move("Invalid Move", 0, '')
INVALID_POKEMON = Pokemon("MissingNo.", 0, [], '', 0)

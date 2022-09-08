from pokemon import Pokemon, Move


def create_team():
    """
    Build a list of Pokemon in this function, and return the list.
    
    The team that you build here will be used as your team in the Pokemon
    tournament.

    """

    thunderShock = Move("Thunder Shock", 50, "electric")
    
    pikachu1 = Pokemon("Pikachu1", 100, [thunderShock], "electric", 80)
    pikachu2 = Pokemon("Pikachu2", 100, [thunderShock], "electric", 80)
    pikachu3 = Pokemon("Pikachu3", 100, [thunderShock], "electric", 80)
    pikachu4 = Pokemon("Pikachu4", 100, [thunderShock], "electric", 80)
    pikachu5 = Pokemon("Pikachu5", 100, [thunderShock], "electric", 80)
    pikachu6 = Pokemon("Pikachu6", 100, [thunderShock], "electric", 80)

    return [pikachu1, pikachu2, pikachu3, pikachu4, pikachu5, pikachu6]


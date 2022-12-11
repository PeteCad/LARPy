# This file contains the database heavy portions of the LARPy application
# Funcions:
#   game_create(game_name)
#           adds a new game to the database
#   user_create(user_name)
#           adds a new user to the database
#   character_create(user_name, game_name, character_name)
#           adds a new user character to a game in the database
import sqlalchemy


def game_create(*args, **kwargs):
    print("Create game code here")

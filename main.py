# Invaders Main program
from game import Game

invaders: Game

if __name__ == "__main__":
    invaders = Game()
    invaders.main_loop()

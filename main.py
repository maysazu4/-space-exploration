import game_logic as g
import persistance as p
import external_data as e
DEFAULT_HEALTH = 100
from spaceship import Spaceship



if __name__ == "__main__":
    print("Lets start our unforgetable adventure in the galaxy !")
    name = input('What is the name of your spaceship?')
    fuel = int(input('How much fuel do you have?'))
    Health = DEFAULT_HEALTH
    spaceShip = Spaceship(name,fuel,Health)
    p.save_spaceship_data(spaceShip)
    e.print_Weather_information()
    while(True):
        if spaceShip.fuel <=0 or spaceShip.health <= 0:
            print('Game Over')
            break
        e = g.chooseRandomEvent()
        g.handle_event(e,spaceShip)


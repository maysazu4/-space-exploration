import random
import time
import math
from spaceship import Spaceship


def chooseRandomEvent():
    e = random.choices(['Asteroid Field','Space Pirates',
                         'Alien Diplomacy', 'Black Hole'])
    return e
    


        
def asteroid_field(spaceship):
    print("Warning: Asteroid Field Ahead!")
    time.sleep(1)
    if isinstance(spaceship,Spaceship):
        decision = input("Do you want to fire at the asteroids (y/n) ? ")
        if decision == 'y':
            time.sleep(1)
            spaceship.fuel -= 5
        elif decision == 'n':
            spaceship.health -= 5

    print('Good job!')
    print('Current fuel:',spaceship.fuel,'Current health:' ,spaceship.health)


def space_pirates(spaceship):
    print('Caution! Infamous space pirates detected in the vicinity')
    if isinstance(spaceship,Spaceship):  
        result = random.choices(['success','fail'])
        print("Get ready – the space pirates are here, and the action's kicking off!")   
        time.sleep(1)
        if result == 'success':
            spaceship.fuel -= 10
        elif result == 'fail':
            spaceship.health -= 10
    print('Good job!')
    print('Current fuel:',spaceship.fuel,'Current health:' ,spaceship.health)


def alien_diplomacy(spaceship):
    print('Prepare for alien diplomacy ...')
    time.sleep(1)
    if random.choices([True,False]):
        print('Your diplomacy efforts have triumphed, the aliens generously offer to replenish your fuel reserves !')
        spaceship.fuel += 30
    else:
        print("The alien diplomats remain unconvinced !")
    print('Current fuel:',spaceship.fuel,'Current health:' ,spaceship.health)



def black_hole(spaceship):
    print("Warninig! There's a massive black hole sucking everything in")
    time.sleep(1)
    print("Increasing the speed ..")
    time.sleep(1)
    spaceship.fuel -= 20
    print('Current fuel:',spaceship.fuel,'Current health:' ,spaceship.health)



def handle_event(event,spaceship):
    match event[0]:
        case 'Asteroid Field':
             asteroid_field(spaceship)
        case 'Space Pirates':
            space_pirates(spaceship)
        case 'Alien Diplomacy':
             alien_diplomacy(spaceship)
        case 'Black Hole':
            black_hole(spaceship)    
        case _:
            return
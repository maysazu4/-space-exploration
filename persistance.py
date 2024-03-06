from spaceship import Spaceship
import json


def convert_spaceship_to_dict(spaceship):
    if isinstance(spaceship,Spaceship):
        dict = {'name' : spaceship.name,
                'fuel' : spaceship.fuel,
                'health' : spaceship.health
                }
    return dict

def convert_dict_to_json(dict):
    json_object = json.dumps(dict, indent=3)
    return json_object

def save_spaceship_data(spaceship):
    dict = convert_spaceship_to_dict(spaceship)
    json_object = convert_dict_to_json(dict) 
    with open("spaceship.json", "w") as outfile:
        outfile.write(json_object)



def load_spaceship_data():
    with open('spaceship.json', 'r') as openfile:
        sData = json.load(openfile)
    return Spaceship(sData["name"], sData["fuel"],sData["health"])
 


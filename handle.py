import math
import json

def dodge_defense_value(obj):
    return (obj["attributes"]["physical"]["dexterity"] +
           obj["abilities"]["dodge"]["dots"] +
           obj["essence"]) * 0.5
        


def parry_defense_value(obj):
    return (obj["attributes"]["physical"]["dexterity"] + 
            obj["abilities"]["melee"]["dots"] +
            obj["weapons and armor"]["grand soulsteel goremaul"]["defense"]) * 0.5


def mental_defense_value(obj):
    return (obj["willpower"] + obj["abilities"]["integrity"]["dots"] + obj["essence"]) * 0.5


def attack_dice_pool(obj, weapon):
    return (
                obj["attributes"]["physical"]["dexterity"] + 
                obj["weapons and armor"][weapon]["accuracy"] + 
                obj["abilities"]["melee"]["dots"]
           )


def damage(obj, weapon):
    return ( 
                obj["attributes"]["physical"]["strength"] +
                obj["weapons and armor"][weapon]["damage"] 
           ) 


def personal_essence_pool(obj):
    return (
                obj["essence"] * 3 +
                obj["willpower"]
           )


def peripheral_essence_pool(obj):
    virtues_sum = 0
    for x in obj["virtues"]:    
        virtues_sum += obj["virtues"][x]
    return (
                obj["essence"] * 7 +
                obj["willpower"] + virtues_sum
                
           )


def main(): 
    f = open("character_sheet.json")
    obj = json.load(f)
    print "peripheral essence pool", peripheral_essence_pool(obj)
    print "personal essence pool", personal_essence_pool(obj)
    print "damage pool", damage(obj, "grand soulsteel goremaul")
    print "attack dice pool", attack_dice_pool(obj, "grand soulsteel goremaul")
    print "mental defense value", mental_defense_value(obj)
    print "parry defense value", parry_defense_value(obj)
    print "dodge defense value", dodge_defense_value(obj) 

if __name__ == "__main__":
    main() 

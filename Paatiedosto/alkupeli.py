import fuktion2
import fuktion1
import random1
import random
import time
from colorama import Fore, Back, Style, init
from Paatiedosto.random1 import my_dictionary, random_key

print("""
         |========================================[-][o][x]|
         |                                                 |                                               
         |               'TERVETULOA PELI!'                |
         |                                                 |                                                                                                |
         |=================================================|    """)
init()
print(Fore.RED + 'GAME GUIDE'+ Style.RESET_ALL)

texto ="""HELLO, AGENT. YOUR MISSION BEGINS NOW!
THE GAME STARTS BY SAVING YOUR DATA.
YOU WILL BE TRAVELING THROUGH DIFFERENT AIRPORTS,
 TRYING TO CAPTURE THE VILLAIN. DURING YOUR TRAVELS, 
 YOU MUST KEEP TRACK OF YOUR FUEL LEVEL, 
 AND YOU WILL NEED TO ROLL THE DICE TO REFUEL. 
 IF YOU GUESS THE CHALLENGE CORRECTLY, YOU'LL BE ABLE TO REFUEL, 
 BUT IF NOT, YOUR FUEL LEVEL WILL DECREASE.
YOU WILL ALSO ASK AT EACH AIRPORT IF THE VILLAIN IS THERE. 
IF NOT, YOU WILL NEED TO SWITCH TO ANOTHER AIRPORT
"""
palabras = texto.split()
pausa = 0.5
limite_caracteres = 50
contador_caracteres = 0
for palabra in palabras:
    if contador_caracteres + len(palabra) > limite_caracteres:
        print()
        contador_caracteres = 0
    print(palabra, end=' ', flush=True)
    contador_caracteres += len(palabra) + 1
    time.sleep(pausa)
print()

print("REGISTER: ")
first_name=input("FIRST_NAME: ")
last_name=input("LAST_NAME: ")
age=int(input("AGE: "))
#birthdate= input("birthdate:")
#Function 2 records in the database
fuktion2.date(first_name,last_name, age)

print("""
        CONTINENT :
        Asia            =   AS
        Africa          =   AF
        North America   =   NA
        South America   =   SA
        Antarctica      =   AT
        Europe          =   EU
        Australi        =   AU
        """)

#valita continet
Play_start = input("WHERE DO YOU WANT TO START? CHOOSE THE CONTINET: ")
continet={"AS":"Asia", "AF":"Africa", "NA":"North_America", "SA":"South_America", "AT":"Antarctica", "EU":"Europe", "AU":"Australi"}

#valita lento kone
konet = {"pieni":"AIRBUS 319", "keski_kokoine":"AIRBUS 321" ,"iso":"BOEING 777" }
lentokone=input( '  "small" "medium_size" "largel" \n cherish the airplane :" ')
gas1= "10"
gas2= "20%"
gas3= "40%"
gas4= "60%"
level = 1
if Play_start in continet:
    print(f"Your mission begins now you are on the continent of {continet[Play_start]}")
    country = fuktion1.continet(Play_start)
    print(f"sinun peli alka kaupungissa {country}")
if lentokone in konet:
    if lentokone=="small":
        print(f" GAS IS {gas1}")
        print(f"LEVEL IS {level}")
    elif lentokone=="medium_size":
        print(f" GAS IS {gas2}")
        print(f"LEVEL IS {level}")
    elif lentokone=="largel":
        print(f" GAS IS {gas3}")
        print(f" LEVEL IS {level}")
print(f"YOU HAVE ARRIVED IN THE CITY {country} IT SEEMS YOU STARTED OUT WITH BAD LUCK.\n"
      f" THE THIEF IS NOT HERE. ROLL THE DICE TO FLY TO THE NEXT CITY")
game_dice = input('ROLL THE DICE "D": ')
if game_dice== "D":
    print(country)


door= input('CHOOSE THE DOOR "A" "B" "C":')
if door=="A":
    print(f" {my_dictionary[random_key]}")









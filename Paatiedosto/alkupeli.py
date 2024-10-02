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

text1 ="""HELLO, AGENT. YOUR MISSION BEGINS NOW!
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
#make the text go slowly
text = text1.split()
pause = 0.2
character_limit = 50
character_counter = 0
for word in text:
    if character_counter+ len(word) > character_limit:
        print()
        character_counter= 0
    print(word, end=' ', flush=True)
    character_counter += len(word) + 1
    time.sleep(pause)
print()
#====
#change text color
print(Fore.RED+"REGISTER:+"+Style.RESET_ALL)
#===
first_name=input("FIRST_NAME: ")
last_name=input("LAST_NAME: ")
age=int(input("AGE: "))
#birthdate= input("birthdate:")
#Function 2 records in the database
fuktion2.date(first_name,last_name, age)

print("""
        ======================
        CONTINENT :
        Asia            =   AS
        Africa          =   AF
        North America   =   NA
        South America   =   SA
        Antarctica      =   AT
        Europe          =   EU
        Australi        =   AU
        ======================
        """)


Play_start = input("WHERE DO YOU WANT TO START\n CHOOSE THE CONTINET: ")
continet={"AS":"Asia", "AF":"Africa", "NA":"North_America", "SA":"South_America", "AT":"Antarctica", "EU":"Europe", "AU":"Australi"}

#valita lento kone
konet = {"small":"AIRBUS 319", "medium_size":"AIRBUS 321" ,"large":"BOEING 777" }
print("""
=====================

        "SMALL"  = S
  "MEDIUM_SIZE"  = M 
        "LARGE"  = L
=====================
        """)


lentokone=input( " CHERISH THE AIRPLANE :")
gas1= "10"
gas2= "20%"
gas3= "40%"
gas4= "60%"
gas5= "80%"
gas6= "100%"
level = 1
if Play_start in continet:
    print(f"Your mission begins now you are on the continent of {continet[Play_start]}")
    country = fuktion1.continet(Play_start)
    print(f"sinun peli alka kaupungissa {country}")
if lentokone in konet:
    if lentokone=="S":
        print(f" GAS IS {gas1}")
        print(f"LEVEL IS {level}")
    elif lentokone=="S":
        print(f" GAS IS {gas2}")
        print(f"LEVEL IS {level}")
    elif lentokone=="L":
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









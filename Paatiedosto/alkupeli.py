import fuktion2
import fuktion1
import random1
import random

from Paatiedosto.random1 import my_dictionary, random_key

print("""
         |========================================[-][o][x]|
         |                                                 |                                               |
         |               'TERVETULOA PELI!'                |
         |                                                 |                                                 |                                                |
         |=================================================|    """)

print("GAME GUIDE")
print("""
Hello, Agent. Your mission begins now!
The game starts by saving your data.
You will be traveling through different airports,
 trying to capture the villain. During your travels, 
 you must keep track of your fuel level, 
 and you will need to roll the dice to refuel. 
 If you guess the challenge correctly, you'll be able to refuel, 
 but if not, your fuel level will decrease.
You will also ask at each airport if the villain is there. 
If not, you will need to switch to another airport.""")


print("REGISTER: ")
first_name=input("FIRST_NAME: ")
last_name=input("LAST_NAME: ")
age=int(input("AGE: "))
#birthdate= input("birthdate:")
#Function 2 records in the database
fuktion2.date(first_name,last_name, age)

print("""
        CHOOSE THE CONTINENT WHERE YOU WANT TO PLAY
        Asia            =   AS
        Africa          =   AF
        North America   =   NA
        South America   =   SA
        Antarctica      =   AT
        Europe          =   EU
        Australi        =   AU
        """)

gas1= "20L"
gas2= "40L"
gas3= "60L"
level = 1
#valita continet
Play_start = input("WHERE DO YOU WANT TO START? CHOOSE THE CONTINET: ")


continet={"AS":"Asia", "AF":"Africa", "NA":"North_America", "SA":"South_America", "AT":"Antarctica", "EU":"Europe", "AU":"Australi"}
#valita lento kone
konet = {"pieni":"AIRBUS 319", "keski_kokoine":"AIRBUS 321" ,"iso":"BOEING 777" }
lentokone=input( '  "small" "medium_size" "largel" \n cherish the airplane :" ')

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
print(f"YOU HAVE ARRIVED IN THE CITY {country} IT SEEMS THE THIEF IS NO LONGER THERE WHO CHOOSES ONE OF THE DOORS TO SEE IF HE IS HERE")
door= input('CHOOSE THE DOOR "A" "B" "C":')
if door=="A":
    print(f" {my_dictionary[random_key]}")









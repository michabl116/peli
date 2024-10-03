from traceback import print_tb

import test2
import fuktion2
import fuktion1
import random1
import random
import time
from colorama import Fore, Back, Style, init

from Paatiedosto import text_fuktion, fuktion3,tunus
from Paatiedosto.random1 import dictionary_A, random_key, dictionary_A, dictionary_B


print("""
         |========================================[-][o][x]|
         |                                                 |                                               
         |               'TERVETULOA PELI!'                |
         |                                                 |                                                                                                |
         |=================================================|    """)
init()
print(Fore.RED + 'GAME GUIDE'+ Style.RESET_ALL)

Text1 ="""AGENT, YOUR MISSION STARTS NOW:
FIRST, YOU MUST REGISTER.
 THEN, YOU WILL CHOOSE THE CONTINENT 
 WHERE YOU WILL START YOUR MISSION, 
 AND AT THE SAME TIME, THE COUNTRY WILL
BE ASSIGNED TO YOU. YOU WILL BE TRAVELING 
THROUGH DIFFERENT AIRPORTS, TRYING TO CAPTURE 
THE VILLAIN WHO HAS STOLEN SECRET INFORMATION. 
DURING YOUR TRAVELS, YOU MUST KEEP TRACK OF 
YOUR FUEL LEVEL AND ROLL THE DICE 
TO REFUEL WHEN NECESSARY.
ADDITIONALLY, YOU WILL FACE VARIOUS CHALLENGES 
ALONG THE WAY, WHICH WILL BE EXPLAINED TO YOU AS 
YOU PROGRESS. THE VILLAIN ISN'T VERY CLEVER AND WILL 
LEAVE YOU CLUES AT EACH AIRPORT. 
ONE OF THE MAIN OBSTACLES WILL BE THE CONSTANT 
DECREASE IN FUEL, SO YOU MUST BE VERY CAREFUL.

GOOD LUCK, OFFICER!
"""
text_fuktion.print_with_delay(Text1)
#make the text go slowly

#====

#change text color
print(Fore.RED+"REGISTER:"+Style.RESET_ALL)
#===
first_name=input("FIRST_NAME: ")
last_name=input("LAST_NAME: ")
age=int(input("AGE: "))
#Function 2 records in the database
fuktion2.date(first_name,last_name, age)
codigo_aleatorio = tunus.generar_codigo()
print("Código aleatorio:", codigo_aleatorio)

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
continet={"AS":"Asia", "AF":"Africa", "NA":"North_America", "SA":"South_America", "AT":"Antarctica", "EU":"Europe", "AU":"Australi"}

Play_start = input("WHERE DO YOU WANT TO START\n CHOOSE THE CONTINET: ")
konet = {"S":"AIRBUS 319", "M":"AIRBUS 321" ,"L":"BOEING 777" }
print("""
=====================
   AIRCRAFT MODELS
        "SMALL"  = S
  "MEDIUM_SIZE"  = M 
        "LARGE"  = L
=====================
        """)
lentokone=input( " CHERISH THE AIRPLANE :")
gas1= 10
gas2= 20
gas3= 40
gas4= 60
gas5= 80
gas6= 100
level = 1
leve2 = 2
if lentokone in konet:
    if lentokone=="S":
        print(f" GAS IS {gas6}")

    elif lentokone=="M":
        print(f" GAS IS {gas5}")

    elif lentokone=="L":
        print(f" GAS IS {gas4}")

if Play_start in continet:
    print(f"YOUR MISSION BEGINS!\n YOU WILL START ON THE CONTINENT {Fore.RED + continet[Play_start]+ Style.RESET_ALL}")
    country = fuktion1.continet(Play_start)
    print(f"  IN THE COUNTRY OF {Fore.RED +country + Style.RESET_ALL} ")


    city2 = fuktion3.airport_name_city(country)
    print(F"AIRPORT NAME IS {Fore.RED+city2[0]+Style.RESET_ALL} IS LOCATE {Fore.RED+city2[1]+Style.RESET_ALL}")
print()
print()

Text2 = """IT SEEMS THAT THIS IS VERY BAD LUCK.
        THE THIEF IS VERY FAST AND IS NO LONGER AT 
        THIS AIRPORT. ROLL THE DICE TO JUMP TO THE 
        NEXT AIRPORT"""
text_fuktion.print_with_delay(Text2)
print()
print()
#heito noppaa
game_dice = input('ROLL THE DICE "D": ')
if game_dice== "D":
    if Play_start in continet:
        country = fuktion1.continet(Play_start)
        print(f"YOU HAVE ARRIVED IN THE CITY OF {Fore.RED+country+Style.RESET_ALL}")
print()
print()
Text3 ="""IT SEEMS THE VILLAIN HAS BEEN TO THIS AIRPORT, BUT
   HE’S NOT CLEVER ENOUGH AND HAS LEFT YOU CLUES. 
   YOU HAVE THREE GATES TO CHOOSE FROM, BUT IF YOU PICK 
   THE WRONG ONE, YOU COULD RUN INTO TROUBLE. 
   GOOD LUCK!
"""
text_fuktion.print_with_delay(Text3)



door= input('CHOOSE THE DOOR "A" "B" "C":')
if door=="A":
    print(f"{dictionary_A[random_key]}")
if door=="B":
    print(f"{dictionary_B[random_key]}")








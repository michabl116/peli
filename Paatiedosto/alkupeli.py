from traceback import print_tb

import test2
import fuktion2
import fuktion1
import random1
import random
import time
from colorama import Fore, Back, Style, init

from Paatiedosto import text_fuktion, fuktion3, tunus, testi



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
ident= tunus.agenti_tunus()
age=int(input("AGE: "))
#Function 2 records in the database
fuktion2.date(first_name,last_name,ident, age)
print("YOUR ADVICE KEY IS:", ident)


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
less_gasoline= -10
less_gasoline= -20
less_gasoline= -50
level = 1
leve2 = 2
leve3 = 3
points1 = 500
points2 = 1000
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

Text2 = """
        IT SEEMS THAT THE THIEF IS NO LONGER 
        HERE, ROLL THE DICE TO JUMP TO THE 
        NEXT AIRPORT """
text_fuktion.print_with_delay(Text2)
print()

#heito noppaa
game_dice = input('ROLL THE DICE "D": ')
if game_dice== "D":
    if Play_start in continet:
        country = fuktion1.continet(Play_start)
        city2 = fuktion3.airport_name_city(country)
        print(f"YOU HAVE ARRIVED IN THE CITY OF {Fore.RED+country+Style.RESET_ALL}")
        print(f"el aeropuerto es{Fore.RED+city2[0]+Style.RESET_ALL} y la ciuda de {Fore.RED+city2[1]+Style.RESET_ALL}")

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
    elect_A = random1.get_random_value_as_int()
    if int(elect_A) <0:
        print(f" I'M SORRY YOUR FUEL HAS DECREASED {elect_A}%" )
    if int(elect_A) >0 and int(elect_A)<= 100  :
        print(f" YOUR FUEL HAS INCREASED BY {elect_A}%" )
    if int(elect_A) >= 500 and int(elect_A) <= 1000:
            print(f" YOU HAVE OBTAINED THE CREDIT OF {elect_A}%")


elif door=="B":
    elect_B = random1.get_random_value_as_int()
    if int(elect_B) < 0:
        print(f" Lo siento tu conbustible a disminido el {elect_B}%")
    elif int(elect_B) > 0 and int(elect_B) <= 100:
        print(f" tu conbible a aumetado un {elect_B}%")
    elif int(elect_B) >= 500 and int(elect_B) <= 1000:
        print(f" as obtenido credito {elect_B}%")

elif door=="C":
    elect_C = random1.get_random_value_as_int()
    if int(elect_C) < 0:
        print(f" Lo siento tu conbustible a disminido el {elect_C}%")
    elif int(elect_C) > 0 and int(elect_C) <= 100:
        print(f" tu conbible a aumetado un {elect_C}%")
    elif int(elect_C) >= 500 and int(elect_C) <= 1000:
        print(f" as obtenido credito {elect_C}%")


Text4= """
         tienes que contiar con con el viaje
         tira nueva mente los dados para saltar
         de aeropuerto 
         el malechor puede estar en el siginete
        """
text_fuktion.print_with_delay(Text4)
print()
game_dice = input('ROLL THE DICE "D": ')
if game_dice== "D":
    if Play_start in continet:
        country = fuktion1.continet(Play_start)
        city2 = fuktion3.airport_name_city(country)
        print(f"YOU HAVE ARRIVED IN THE CITY OF {Fore.RED+country+Style.RESET_ALL}")
        print(f"el aeropuerto es{Fore.RED+city2[0]+Style.RESET_ALL} y la ciuda de {Fore.RED+city2[1]+Style.RESET_ALL}")
Text5 = """ 
        denitiva  estas serca de capturar 
        malechor  eleje uan puera para optener 
        alguna reconpensa o
        dificultad
        """
text_fuktion.print_with_delay(Text5)
print()
door= input('CHOOSE THE DOOR "A" "B" "C":')
if door=="A":
    elect_D = random1.get_random_value_as_int()
    if int(elect_D) <0:
        print(f" Lo siento tu conbustible a disminido el {elect_D}%" )
    elif int(elect_D) >0 and int(elect_D)<= 100  :
        print(f" tu conbible a aumetado un {elect_D}%" )
    elif int(elect_D) >= 500 and int(elect_D) <= 1000:
            print(f" as obtenido credito {elect_D}%")


elif door=="B":
    elect_E = random1.get_random_value_as_int()
    if int(elect_E) < 0:
        print(f" Lo siento tu conbustible a disminido el {elect_E}%")
    elif int(elect_E) > 0 and int(elect_E) <= 100:
        print(f" tu conbible a aumetado un {elect_E}%")
    elif int(elect_E) >= 500 and int(elect_E) <= 1000:
        print(f" as obtenido credito {elect_E}%")


elif door=="C":
    elect_f = random1.get_random_value_as_int()
    if int(elect_f) < 0:
        print(f" Lo siento tu conbustible a disminido el {elect_f}%")
    elif int(elect_f) > 0 and int(elect_f) <= 100:
        print(f" tu conbible a aumetado un {elect_f}%")
    elif int(elect_f) >= 500 and int(elect_f) <= 1000:
        print(f" as obtenido credito {elect_f}%")



































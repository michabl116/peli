import fuktion2
import fuktion

print("""
         |========================================[-][o][x]|
         |                                                 |
         |                                                 |
         |               'TERVETULOA PELI!'                |
         |                                                 |
         |                                                 |
         |                                                 |
         |=================================================|    """)



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




print(" täytä tietosi:")
first_name=input("name:")
last_name=input("lastname:")
age=int(input("age:"))
#birthdate= input("birthdate:")
fuktion2.date(first_name,last_name, age)

print("GAME GUIDE")



print("""
        Choose the continent where you want to play
        Asia            =   AS
        Africa          =   AF
        North America   =   NA
        South America   =   SA
        Antarctica      =   AT
        Europe          =   EU
        Australi        =   AU
        """)

vensa= "20L"
taso = 1
#valita continet
Play_start = input("WHERE DO YOU WANT TO START? CHOOSE THE CONTINET: ")


continet={"AS":"Asia", "AF":"Africa", "NA":"North_America", "SA":"South_America", "AT":"Antarctica", "EU":"Europe", "AU":"Australi"}
#valita lento kone
konet = {"pieni":"AIRBUS 319", "keski_kokoine":"AIRBUS 321" ,"iso":"BOEING 777" }
lentokone=input( '  "pieni" "keski_kokoine" "iso" \n vaalitse lentokone :" ')

if Play_start in continet:
    if lentokone in konet:
        if lentokone=="pieni":
            print(f"Your mission begins now you are on the continent of {continet[Play_start]}")
            fuktion.continet(Play_start)
            print(f" venssa mara on {vensa}")
            print(f"sun taso on {taso}")







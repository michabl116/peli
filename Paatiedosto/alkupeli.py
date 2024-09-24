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


print("Ennen aloittamista täytä tietosi")
first_name=input("name:")
last_name=input("lastname:")
age=int(input("age:"))
#birthdate= input("birthdate:")
fuktion2.date(first_name,last_name, age)

print("GAME GUIDE")

print("Hello Agent 007, your mission begins. Choose the continent where you want to play.")

print("""
        Asia            =   AS
        Africa          =   AF
        North America   =   NA
        South America   =   SA
        Antarctica      =   AT
        Europe          =   EU
        Australi        =   AU
        """)

Play_start = input("WHERE DO YOU WANT TO START? CHOOSE THE CONTINET: ")
fuktion.continet(Play_start)
continet={"AS":"Asia", "AF":"Africa", "AF":"North_America", "SA":"South_America", "AT":"Antarctica", "EU":"Europe", "AU":"Australi"}

if Play_start in continet:
    print(f"Your mission begins now you are on the continent of {continet[Play_start]}")








#lentokone=input( '  "AIBUS 319" "AIRBUS 321" "BOEING 777" \n vaalitse lentokone :" ')





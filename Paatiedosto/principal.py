import subprocess

from Paatiedosto import text_fuktion
print("""
    
   0=======================0    
   0      LENTO PELIT      0
   0                       0
   0=======================0 """)

print()

texti="""TERVETULOA PELEIMME!
         SINULLA ON KOLME PELIä, JOISTA VALITTAA
         PITÄÄ HAUSKAA!
           
           
           """

text_fuktion.print_with_delay(texti)
print()
print("TEKIJAT")
print()
print("ARTEM\nMATIAS\nFARHAM\nMICAHEL")
print()
nimi= input("ANNA PELI NIMI:")
if nimi == "peli1":
    subprocess.run(["python", "alkupeli.py"])

if nimi == "peli2":
    subprocess.run(["python", "alkupeli.py"])
if nimi == "peli3":
    subprocess.run(["python", "alkupeli.py"])
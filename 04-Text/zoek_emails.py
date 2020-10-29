import re

emails = []

with open("tekstmetemails.txt", "r") as bestand:

    regel = bestand.readline()
   
    while regel:

        # Vul de juiste regular expression voor een email in op de puntjes
        patroon = r"[\w+@|]
       

        # Gebruik de juiste code op de plaats van de puntjes
        gevonden = re.findall(patroon, regel)

        emails.extend(regel)
        
        # Volgende regel lezen
        regel = bestand.readline()

print(emails)

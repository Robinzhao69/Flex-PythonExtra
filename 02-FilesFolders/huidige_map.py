import os

werkmap = os.getcwd()

print("De huidige map is: " + werkmap)



mapnaam = ""

lengte_mapnaam = 0

while lengte_mapnaam == 0:
    mapnaam = input("Welke naam wil je voor de map")

# Sla de lengte van de mapnaam op in de variabele lengte_mapnaam
    lengte_mapnaam = len(mapnaam)


# Sla de lengte van de mapnaam op in de variabele lengte_mapnaam
    if lengte_mapnaam > 0:
        os.mkdir(mapnaam)
    else:
# En anders melden we dat er niets is ingevuld
        print("Je hebt geen naam ingevoerd")
    

# ... en anders gaat de code hier verder
print("De map " + mapnaam + " is gemaakt.")


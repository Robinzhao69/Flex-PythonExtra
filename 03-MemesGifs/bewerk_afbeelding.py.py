from PIL import Image

afbeelding = Image.open("chokings.jpg")

afbeelding.show()


breedte = afbeelding.width
hoogte = afbeelding.height


helft_breedte = afbeelding.width // 2
helft_hoogte = afbeelding.height // 2

# Met het resize commando kun je de afmetingen van afbeelding aanpassen
# Deze verwacht een Tuple variabele:
nieuwe_afmeting = (helft_breedte, helft_hoogte)

# Hier wordt de afbeelding kleiner gemaakt en opgeslagen in een nieuwe variabele!
kleinere_afbeelding = afbeelding.resize(nieuwe_afmeting)

# Nu de kleinere afbeelding opslaan me save(). Gebruik de originele bestandsnaam met ergens "klein" er in. 
kleinere_afbeelding.save("chokings.jpg")


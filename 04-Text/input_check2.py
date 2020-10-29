import re


while True:

    postcode = input("Voer je postcode in: ")

    patroon = r"\d{4}\s?\D{2}$"
    matches = re.findall(patroon, postcode)

    if(len(matches) > 0):
        break
print("bedankt voor je postcode:", matches[0])

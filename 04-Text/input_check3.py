import re


while True:

    kenteken = input("voer hier je kenteken in: ")

    patroon = r"[A-Z]{2}-\d{3}-[A-Z]{3}"

    matches = re.findall(patroon, kenteken)

    if(len(matches) > 0):
        break

print("bedankt voor je kenteken.", matches[0])

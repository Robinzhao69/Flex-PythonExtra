from PIL import Image, ImageFont, ImageDraw

afbeelding = Image.open("meme_background.jpg")

breedte = afbeelding.width
hoogte = afbeelding.height

print("De afbeelding is " + str(breedte) + " pixels breed en " + str(hoogte) + " pixels hoog")
print(afbeelding.format, afbeelding.size, afbeelding.mode)

lettertype = ImageFont.truetype("impact.ttf", 30)
tekengebied = ImageDraw.Draw(afbeelding)

tekst = "Are ya winning son?"
tekengebied.multiline_text((10,10), tekst, font=lettertype, fill=(0,0,0))

afbeelding.show()
afbeelding.save("meme_met_tekst_Xd.jpg")


kaasGeel = input("is de kaas geel? ")

if kaasGeel == "ja":
   kaasGaten = input("zitten er gaten in? ")

if kaasGeel == "nee":
   kaasSchimmel = input("heeft de kaas blauwe schimmel? ")

if kaasSchimmel == "ja":
   kaasRechts = input("heeft de kaas een korst? ")

if kaasSchimmel == "nee":
   kaasLinks = input("heeft de kaas een korst? ")

if kaasLinks == "ja":
   print("Camembert")

if kaasLinks == "nee":
   print("Mozzarella")

if kaasRechts == "ja":
   print("Blue de Rochbaron")

if kaasRechts == "nee":
   print("Foume d Ambert")

if kaasGaten == "ja":
   kaasDuur = input("is de kaas belachelijk duur? ")

if kaasGaten == "nee":
   kaasHard = input("is de kaas hard als steen? ")

if kaasDuur == "ja":
   print("Emmenthaler")

if kaasDuur == "nee":
   print("Leerdammer")

if kaasHard == "ja":
   print("Parmigiano Reggiano")

if kaasHard == "nee":
   print("Goudse Kaas")
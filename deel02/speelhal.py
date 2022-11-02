aantal_mensen = 4
toegangsprijs = 7.45
vip = 0.37

aantalMensen = int(input("met hoeveel mensen ben je? "))
print("je ben met dit aantal mensen", aantalMensen)

aantalMinuten = int(input("hoeveel minuten willen jullie in de vip? "))
print("je wilt dit aantal minuten in de vip", aantalMinuten)

bedrag = (aantalMensen * toegangsprijs + aantalMinuten * vip)
print("dit geweldige dagje met",aantalMensen,"mensen in de speelhal en",aantalMinuten,"minuten VIP kostte me", bedrag, "euro")
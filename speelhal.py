aantal_mensen = 4
toegangsprijs = 7.45
vip = 0.37

txt_1 = input("met hoeveel mensen ben je? ")
aantal_1 = int(txt_1)
print("je ben met dit aantal mensen", aantal_1)

txt_2 = input("hoeveel minuten willen jullie in de vip? ")
aantal_2 = int(txt_2)
print("je wilt dit aantal minuten in de vip", aantal_2)

bedrag = (aantal_mensen * toegangsprijs + aantal_2 * vip)
print("dit geweldige dagje met 4 mensen in de speelhal met 45 minuten VIP kostte me", bedrag, "euro")
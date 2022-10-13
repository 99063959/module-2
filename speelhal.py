aantal_mensen = 4
toegangsprijs = 7.45
vip = 0.37

aantal_1 = int(input("met hoeveel mensen ben je? "))
print("je ben met dit aantal mensen", aantal_1)

aantal_2 = int(input("hoeveel minuten willen jullie in de vip? "))
print("je wilt dit aantal minuten in de vip", aantal_2)

bedrag = (aantal_1 * toegangsprijs + aantal_2 * vip)
print("dit geweldige dagje met",aantal_1,"mensen in de speelhal en",aantal_2,"minuten VIP kostte me", bedrag, "euro")
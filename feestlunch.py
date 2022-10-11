croissant = 0.39
stokbroden = 2.78
kortingsbon = 0.50

aantal_1 = int (input("hoeveel croissants wilt uw? "))
#aantal_1 = int(txt_1)
print("uw heeft dit aantal croissants besteld", aantal_1)

txt_2 = input("hoeveel stokbroden wilt uw? ")
aantal_2 = int(txt_2)
print("uw heeft dit aantal stokbroden besteld", aantal_2)

txt_3 = input("hoeveel kortingsbonnen heeft uw? ")
aantal_3 = int(txt_3)
print("uw heeft dit aantal kortingsbonnen", aantal_3)

bedrag = (aantal_1 * croissant + aantal_2 * stokbroden + aantal_3 - kortingsbon)
print("de feestlunch kost je bij de bakker", bedrag, "voor de 17 croissantjes en de 2 stokbroden.")
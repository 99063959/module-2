croissant = 0.39
stokbroden = 2.78
kortingsbon = 0.50

aantal_1 = int(input("hoeveel croissants wilt uw? "))
print("uw heeft dit aantal croissants besteld", aantal_1)

aantal_2 = int(input("hoeveel stokbroden wilt uw? "))
print("uw heeft dit aantal stokbroden besteld", aantal_2)

aantal_3 = int(input("hoeveel kortingsbonnen heeft uw? "))
print("uw heeft dit aantal kortingsbonnen", aantal_3)

bedrag = (aantal_1 * croissant + aantal_2 * stokbroden + aantal_3 - kortingsbon)
print("de feestlunch kost je bij de bakker", bedrag, "voor de" ,aantal_1,"croissantjes en de",aantal_2,"stokbroden.")
croissant = 0.39
stokbroden = 2.78
kortingsbon = 0.50

aantalCroissant = int(input("hoeveel croissants wilt uw? "))
print("uw heeft dit aantal croissants besteld", aantalCroissant)

aantalStokbrood = int(input("hoeveel stokbroden wilt uw? "))
print("uw heeft dit aantal stokbroden besteld", aantalStokbrood)

aantalKortingsbon = int(input("hoeveel kortingsbonnen heeft uw? "))
print("uw heeft dit aantal kortingsbonnen", aantalKortingsbon)

bedrag = (aantalCroissant * croissant + aantalStokbrood * stokbroden + aantalKortingsbon - kortingsbon)
print("de feestlunch kost je bij de bakker", bedrag, "voor de" ,aantalCroissant,"croissantjes en de",aantalStokbrood,"stokbroden.")
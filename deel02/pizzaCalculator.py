prijsSmall = 8
prijsMedium = 9
prijsLarge = 10
notstop = True
aantalSmall = 0
aantalMedium = 0
aantalLarge = 0
bedragTotaal = 0

while notstop:
    afmeting = input("wat voor maat pizza wil je small, medium of large? ")

    if afmeting == "small":
        aantalSmall = int(input("hoeveel small pizzas wil je? "))
        print("je hebt",aantalSmall,"small pizzas besteld")

    elif afmeting == "medium":
        aantalMedium = int(input("hoeveel medium pizzas wil je? "))
        print("je hebt",aantalMedium,"medium pizzas besteld")
            
    elif afmeting == "large":
        aantalLarge = int(input("hoeveel large pizzas wil je? "))
        print("je hebt",aantalLarge,"large pizzas besteld")
    
    elif afmeting == "stop":
        notstop = False
        bedragTotaal += (aantalSmall * prijsSmall)
        bedragTotaal += (aantalMedium * prijsMedium)
        bedragTotaal += (aantalLarge * prijsLarge)
        print("het aantal smalle pizzas besteld is",aantalSmall,"waarvan de prijs is",aantalSmall * prijsSmall,"euro")
        print("het aantal medium pizzas besteld is",aantalMedium,"waarvan de prijs is",aantalMedium * prijsMedium,"euro")
        print("het aantal large pizzas besteld is",aantalLarge,"waarvan de prijs is",aantalLarge * prijsLarge,"euro")
        print("het totaal bedrag is",bedragTotaal,"euro")
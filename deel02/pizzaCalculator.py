prijsSmall = 8
prijsMedium = 9
prijsLarge = 10
notstop = True

while notstop:
    afmeting = input("wat voor maat pizza wil je small, medium of large? ")
   
    if afmeting == "stop":
        notstop = False
        bedragSmall = (aantalSmall * prijsSmall)
        bedragMedium = (aantalMedium * prijsMedium)
        bedragLarge = (aantalLarge * prijsLarge)
        bedrag = (bedragSmall + bedragMedium + bedragLarge)
        print("het bedrag wat je moet betalen voor de pizzas is" ,bedrag)

    elif afmeting == "small":
        aantalSmall = int(input("hoeveel small pizzas wil je? "))
        print("je hebt",aantalSmall,"small pizzas besteld")

    elif afmeting == "medium":
        aantalMedium = int(input("hoeveel medium pizzas wil je? "))
        print("je hebt",aantalMedium,"medium pizzas besteld")
            
    elif afmeting == "large":
        aantalLarge = int(input("hoeveel large pizzas wil je? "))
        print("je hebt",aantalLarge,"large pizzas besteld")
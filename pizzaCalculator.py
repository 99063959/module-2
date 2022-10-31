prijsSmall = 8
prijsMedium = 9
prijsLarge = 10

afmeting = input("wat voor maat pizza wil je small, medium of large? ")

if afmeting == "small":
    aantal = int(input("hoeveel small pizzas wil je? "))
    print("je hebt",aantal,"small pizzas besteld")
    bedrag = (prijsSmall * aantal)
    print("het bedrag wat je moet betalen is",bedrag,"euro")

elif afmeting == "medium":
    aantal = int(input("hoeveel medium pizzas wil je? "))
    print("je hebt",aantal,"medium pizzas besteld")
    bedrag = (prijsMedium * aantal)
    print("het bedrag wat je moet betalen is",bedrag,"euro")
    
elif afmeting == "large":
    aantal = int(input("hoeveel large pizzas wil je? "))
    print("je hebt",aantal,"large pizzas besteld")
    bedrag = (prijsLarge * aantal)
    print("het bedrag wat je moet betalen is",bedrag,"euros")
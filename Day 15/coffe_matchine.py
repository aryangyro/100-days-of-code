MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
dime = 0.01
nickle = 0.1
quarter = 0.25
dollar = 1

nowater = False
nomilk = False
nocoffee = False


run = True

while run:
    a = input("What do you want : \n Type a for capachino \n Type b for latte \n Type c for espresso :").lower()

    if a == "report":
        print(resources)

    elif a == "a":
        supply1 = resources["water"]
        supply2 = resources["milk"]
        supply3 = resources["coffee"]

        req1 = MENU["cappuccino"]["ingredients"]["water"]
        req2 = MENU["cappuccino"]["ingredients"]["milk"]
        req3 = MENU["cappuccino"]["ingredients"]["coffee"]



        if supply1 < req1:
            nowater = True
        if supply2 < req2:
            nomilk = True
        if supply3 < req3:
            nocoffee = True

        if nomilk or nocoffee or nowater:
            break

        coin1 = int(input("how many dimes are you giving :"))
        coin2 = int(input("how many nickle are you giving :"))
        coin3 = int(input("how many quarter are you giving :"))
        coin4 = int(input("how many dollar are you giving :"))

        total = (coin1*dime) + (coin2*nickle) + (coin3*quarter) + (coin4*dollar)
        print()
        remainder = total - MENU["espresso"]["cost"]
        print()

        resources["water"] -= req1
        resources["milk"] -= req2
        resources["coffee"] -= req3

        print(f"Here's Your change back {remainder} and here's your coffee \n")

    elif a == "b":
        supply1 = resources["water"]
        supply2 = resources["milk"]
        supply3 = resources["coffee"]

        req1 = MENU["latte"]["ingredients"]["water"]
        req2 = MENU["latte"]["ingredients"]["milk"]
        req3 = MENU["latte"]["ingredients"]["coffee"]

        if supply1 < req1:
            print("\n Sorry, you don't have enough water")
            break
        if supply2 < req2:
            print("\n Sorry, you don't have enough milk")
            break
        if supply3 < req3:
            print("\n Sorry, you don't have enough coffee")
            break

        coin1 = int(input("how many dimes are you giving :"))
        coin2 = int(input("how many nickle are you giving :"))
        coin3 = int(input("how many quarter are you giving :"))
        coin4 = int(input("how many dollar are you giving :"))

        total = (coin1*dime) + (coin2*nickle) + (coin3*quarter) + (coin4*dollar)
        print()
        remainder = total - MENU["latte"]["cost"]
        print()

        resources["water"] -= req1
        resources["milk"] -= req2
        resources["coffee"] -= req3

        print(f"Here's Your change back {remainder} and here's your coffee \n")

    elif a == "c":
        supply1 = resources["water"]
        supply3 = resources["coffee"]

        req1 = MENU["espresso"]["ingredients"]["water"]
        req3 = MENU["espresso"]["ingredients"]["coffee"]

        if supply1 < req1:
            print("\n Sorry, you don't have enough water")
            break
        if supply3 < req3:
            print("\n Sorry, you don't have enough coffee")
            break

        coin1 = int(input("how many dimes are you giving :"))
        coin2 = int(input("how many nickle are you giving :"))
        coin3 = int(input("how many quarter are you giving :"))
        coin4 = int(input("how many dollar are you giving :"))

        total = (coin1*dime) + (coin2*nickle) + (coin3*quarter) + (coin4*dollar)
        print()
        remainder = total - MENU["espresso"]["cost"]
        print()

        resources["water"] -= req1
        resources["coffee"] -= req3

        print(f"Here's Your change back {remainder} and here's your coffee \n")



if nomilk:
    print("\n Sorry, you don't have enough milk")
if nocoffee:
    print("\n Sorry, you don't have enough coffee")
if nowater:
    print("\n Sorry, you don't have enough water")







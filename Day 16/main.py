from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_matchine = MoneyMachine()

cofi_maker = CoffeeMaker()

print()
money_matchine.report()
print()
cofi_maker.report()
print()
work = True

while work:
    menu = Menu()
    item = menu.get_items()
    print()
    ans = input(f"What would you like to have {item} :").lower()
    
    if ans == "report":
        print()
        money_matchine.report()
        cofi_maker.report()
        print()
    
    elif ans == "off":
        work = False
    
    else:
        drink = menu.find_drink(ans)
        
        if drink is None:
            continue
        
        if cofi_maker.is_resource_sufficient(drink) and money_matchine.make_payment(drink.cost):
            print()
            cofi_maker.make_coffee(drink)
        
        
    
    
from data import MENU,resources

"""Needed variables"""

# class Coffee:
#     def __init__(self, name, coffee, water, milk, money):
#         self.type = name
#         self.coffee = coffee
#         self.water = water
#         self.milk = milk
#         self.money = money

# coffee1 = Coffee("espresso", 18, 50, 0, 2.50)
# coffee2 = Coffee("latte", 18, 50, 60, 3.20)
# coffee3 = Coffee("cappuccino", 9, 40, 40, 2.80)

water = resources["water"]
milk = resources["milk"]
coffee = resources["coffee"]
money = 0



def coins():
    quarter = float(input("How many quarters?: ")) * 0.25
    dime = float(input("How many dimes?: ")) * 0.10
    nickle = float(input("How many nickles?: ")) * 0.05
    pennie = float(input("How many pennies?: ")) * 0.01  
    

def coffee_order(order):
    match order:
        case "espresso":
            print("You ordered an Espresso ☕")
            
            if MENU["espresso"]["ingredients"]["water"] > water:
                print("Sorry not enough water")
            elif MENU["espresso"]["ingredients"]["coffee"] > coffee:
                print("Sorry not enough water")
            elif MENU["espresso"]["ingredients"]["milk"] > milk:
                print("Sorry not enough water")
            else:
                coins()
                water -= MENU["espresso"]["ingredients"]["water"]
                milk -= MENU["espresso"]["ingredients"]["milk"]
                coffee -= MENU["espresso"]["ingredients"]["coffee"]
                
            
        case "latte":
            print("You ordered a Latte 🥛☕")
        case "cappuccino":
            print("You ordered a Cappuccino ☁☕")
        case "off":
            print("Shutting down... 📴")
            exit()
        case "report":
            print(f"Water: {water}ml.")
            print(f"Milk: {milk}ml.")  
            print(f"Coffee: {coffee}g.")
            print(f"Money: ${money}")
        case _:
            print("Sorry, we don't have that. 😕")


while True:
    
    userprompt = input("What would you like? (espresso / latte / cappuccino): ").lower()
    
    """Check whether input is valid"""
    while userprompt not in ['espresso', 'latte', 'cappuccino', 'off', 'report']:
        userprompt = input("Sorry, we don't have that. (espresso / latte / cappuccino): ").lower()
    
    coffee_order(userprompt)

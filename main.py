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



def coins(x):
    global money
    
    print("Please insert coins.")
    quarter = float(input("How many quarters?: ")) * 0.25
    dime = float(input("How many dimes?: ")) * 0.10
    nickle = float(input("How many nickles?: ")) * 0.05
    pennie = float(input("How many pennies?: ")) * 0.01
    total = sum([quarter,dime,nickle,pennie])   
    if total < x["cost"]:
        print(f"Sorry that's not enough money. You entered {round(total,2)}, but need {round(x["cost"] - total,2)} more. Money refunded.")
    else:
        money += x["cost"]
        print(f"Here is ${round(total - x["cost"],2)} in change.")
    

def coffee_order(order):
    global water, milk, coffee, money  # Declare these as global
    match order:
        case "espresso":
            
            if MENU["espresso"]["ingredients"]["water"] > water:
                print("Sorry not enough water")
            elif MENU["espresso"]["ingredients"]["coffee"] > coffee:
                print("Sorry not enough water")
            else:
                coins(MENU["espresso"])
                water -= MENU["espresso"]["ingredients"]["water"]
                coffee -= MENU["espresso"]["ingredients"]["coffee"]
                print("You ordered an Espresso ☕")
               
            
        case "latte":
            
            if MENU["latte"]["ingredients"]["water"] > water:
                print("Sorry not enough water")
            elif MENU["latte"]["ingredients"]["milk"] > milk:
                print("Sorry not enough water")
            elif MENU["latte"]["ingredients"]["coffee"] > coffee:
                print("Sorry not enough water")
            else:
                coins(MENU["latte"])
                water -= MENU["latte"]["ingredients"]["water"]
                milk -= MENU["latte"]["ingredients"]["milk"]
                coffee -= MENU["latte"]["ingredients"]["coffee"]
                print("You ordered a Latte 🥛☕")
                  
        case "cappuccino":

            
            if MENU["cappuccino"]["ingredients"]["water"] > water:
                print("Sorry not enough water")
            elif MENU["cappuccino"]["ingredients"]["milk"] > milk:
                print("Sorry not enough water")
            elif MENU["cappuccino"]["ingredients"]["coffee"] > coffee:
                print("Sorry not enough water")
            else:
                coins(MENU["cappuccino"])
                water -= MENU["cappuccino"]["ingredients"]["water"]
                milk -= MENU["cappuccino"]["ingredients"]["milk"]
                coffee -= MENU["cappuccino"]["ingredients"]["coffee"]
                print("You ordered a Cappuccino ☁☕")   
                     
        case "off":
            print("Shutting down... 📴")
            exit()
        case "report":
            print(f"Water: {water}ml.")
            print(f"Milk: {milk}ml.")  
            print(f"Coffee: {coffee}g.")
            print(f"Money: ${money}")
        case "refill":
            milk = 200
            water = 300
            coffee = 100
        case _:
            print("Sorry, we don't have that. 😕")


while True:
    
    userprompt = input("What would you like? (espresso / latte / cappuccino): ").lower()
    
    """Check whether input is valid"""
    while userprompt not in ['espresso', 'latte', 'cappuccino', 'off', 'report', 'refill']:
        userprompt = input("Sorry, we don't have that. (espresso / latte / cappuccino): ").lower()
    
    coffee_order(userprompt)

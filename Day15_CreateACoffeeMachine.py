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


def coin_taker():
    print("Please enter coins.")
    quarters = int(input("How many quarters? :"))
    dimes = int(input("How many dimes? :"))
    nickels = int(input("How many nickels? :"))
    pennies = int(input("How many pennies? :"))
    amount_entered = float(quarters * 0.25 + dimes * 0.1 + nickels * 0.05 + pennies * 0.01)
    
    return round(amount_entered,2)


def profit_teller(choices):
    if choices == "espresso":
        costs = MENU["espresso"]["cost"]
        
    elif choices == "cappuccino":
        costs = MENU["cappuccino"]["cost"]
              
    elif choices == "latte":
        costs = MENU["latte"]["cost"]
        
    change = user_enters_amount - float(costs)
    return round(change,2)

def ingredient_reduction():
    if choice == "espresso" and user_enters_amount >= MENU["espresso"]["cost"]:
        resources["water"] = resources["water"] - MENU["espresso"]["ingredients"]["water"]
        resources["coffee"] = resources["coffee"] - MENU["espresso"]["ingredients"]["coffee"]
    elif choice == "latte" and user_enters_amount >= MENU["latte"]["cost"]:
        resources["water"] = resources["water"] - MENU["latte"]["ingredients"]["water"]
        resources["coffee"] = resources["coffee"] - MENU["latte"]["ingredients"]["coffee"]
        resources["milk"] = resources["milk"] - MENU["latte"]["ingredients"]["milk"]
    elif choice == "cappuccino" and user_enters_amount >= MENU["cappuccino"]["cost"]:
        resources["water"] = resources["water"] - MENU["cappuccino"]["ingredients"]["water"]
        resources["coffee"] = resources["coffee"] - MENU["cappuccino"]["ingredients"]["coffee"]
        resources["milk"] = resources["milk"] - MENU["cappuccino"]["ingredients"]["milk"]


def is_resource_enough(order_ingredients):
  for i in order_ingredients:
    if resources[i] < order_ingredients[i]:
      print(f"Sorry there is not enough {i}")
      return False
  return True


should_play = True
profit_made=0.0
user_enters_amount = 0.0
while should_play:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    #TODO1: if "off" is chosen
    if choice == "off":
      print("Shutting down . . . ")
      should_play = False
    elif choice == "espresso" or choice == "latte" or choice == "cappuccino":
      user_needs= MENU[choice]
      #check for availability
      
      
      
      
      if is_resource_enough(user_needs["ingredients"]):
        user_enters_amount = coin_taker()
        extra_received = profit_teller(choice)
        if extra_received == 0.0:
          ingredient_reduction()
          profit_made+=user_enters_amount-extra_received
          print(f"You have tendered exact change.No returns needed!\nHere is your {choice} ☕.Enjoy!")
        elif extra_received > 0.00:
          ingredient_reduction()
          print(f"Here is ${extra_received} in change.\nHere is your {choice} ☕.Enjoy!")
          profit_made+=user_enters_amount-extra_received
        else:
          print("Sorry that's not enough money. Money refunded")
    elif choice == "report":
      print(f"water : {resources['water']}ml")
      print(f"coffee : {resources['coffee']}g")
      print(f"milk : {resources['milk']}ml")
      print(f"Profit : ${profit_made}")

    else:
      print("Incorrect option chosen!") 

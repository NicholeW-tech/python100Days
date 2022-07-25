import data

def play_game():
    water = 300
    milk = 200
    coffee = 100
    money = 0
    end_of_game = False
    while not end_of_game:
        coffee_type = input("What would you like? (espresso/ latte/ cappuccino)")
        if coffee_type == "espresso":
            coffee_type = data.MENU["espresso"]
            water -= data.MENU["espresso"]["ingredients"]["water"]
            coffee -= data.MENU["espresso"]["ingredients"]["coffee"]
            print("Please insert coins")

            if water <= 0:
                print("Not enough water to make")
                end_of_game = True
                break
            elif milk <= 0:
                print("Not enough milk to make")
                end_of_game = True
                break
            elif coffee <= 0:
                print("Not enough coffee to make")
                end_of_game = True
                break

            quarters = int(input("How many quarters?")) * 0.25
            dimes = int(input("How many dimes?")) * 0.10
            nickles = int(input("How many nickles?")) * 0.05
            sum = round(quarters + dimes + nickles, 2)
            print(sum)
            if sum < data.MENU["espresso"]["cost"]:
                sum -= quarters + dimes + nickles
                print("incorrect funds, please try again")
            elif sum >= data.MENU["espresso"]["cost"]:
                print("here is your espresso!")
                if sum > data.MENU["espresso"]["cost"]:
                    sum -= data.MENU["espresso"]["cost"]
                    rounded = round(sum, 2)
                    print(f"Here is your change ${rounded}")
                money += sum
        elif coffee_type == "latte":
            coffee_type = data.MENU["latte"]
            water -= data.MENU["latte"]["ingredients"]["water"]
            coffee -= data.MENU["latte"]["ingredients"]["coffee"]
            milk -= data.MENU["latte"]["ingredients"]["milk"]
            print("Please insert coins")

            if water <= 0:
                print("Not enough water to make")
                end_of_game = True
                break
            elif milk <= 0:
                print("Not enough milk to make")
                end_of_game = True
                break
            elif coffee <= 0:
                print("Not enough coffee to make")
                end_of_game = True
                break

            quarters = int(input("How many quarters?")) * 0.25
            dimes = int(input("How many dimes?")) * 0.10
            nickles = int(input("How many nickles?")) * 0.05
            sum = round(quarters + dimes + nickles, 2)

            if sum < data.MENU["latte"]["cost"]:
                sum -= quarters + dimes + nickles
                print("incorrect funds, please try again")
            elif sum >= data.MENU["latte"]["cost"]:
                print("here is our latte!")
                if sum > data.MENU["latte"]["cost"]:
                    sum -= data.MENU["latte"]["cost"]
                    rounded = round(sum, 2)
                    print(f"Here is your change ${rounded}")
                money += sum

        elif coffee_type == "cappuccino":
            coffee_type = data.MENU["cappuccino"]
            water -= data.MENU["cappuccino"]["ingredients"]["water"]
            coffee -= data.MENU["cappuccino"]["ingredients"]["coffee"]
            milk -= data.MENU["cappuccino"]["ingredients"]["milk"]
            print("Please insert coins")

            if water <= 0:
                print("Not enough water to make")
                end_of_game = True
                break
            elif milk <= 0:
                print("Not enough milk to make")
                end_of_game = True
                break
            elif coffee <= 0:
                print("Not enough coffee to make")
                end_of_game = True
                break

            quarters = int(input("How many quarters?")) * 0.25
            dimes = int(input("How many dimes?")) * 0.10
            nickles = int(input("How many nickles?")) * 0.05
            sum = round(quarters + dimes + nickles, 2)
            print(sum)
            if sum < data.MENU["cappuccino"]["cost"]:
                sum -= quarters + dimes + nickles
                print("incorrect funds, please try again")
            elif sum >= data.MENU["cappuccino"]["cost"]:
                print("here is our cappuccino!")
                if sum > data.MENU["cappuccino"]["cost"]:
                    sum -= data.MENU["cappuccino"]["cost"]
                    rounded = round(sum, 2)
                    print(f"Here is your change ${rounded}")
                money += sum





play_game()

# In grocery store's stock
print("Logged in Stock Record")
print("At first, let's keep track of eating's staff.\n")

stock = [
    {"fruit": {"apple":10, "orange":5, "pear":7}},
    {"vegetable": {"lettuce":5, "broccoli":7, "tomato":6, "cucumber":9}},
    {"fast_food":{"hamburger":2, "pizza":4, "hot dog":6, "fries":8}},
    {"drink": {"coke":6, "coffee":5, "tea":4, "milk":3}}
         ]
alreadyAte = []

# input_category = input("What kind of food was eaten?\n")
# food = input("What food was eaten?\n")
# person = input("Who ate the food?\n")

def get_category(category):
    for t_category in stock:
        if t_category[category] is not None:
            return t_category

def menu():
    print("\nPress 1: To add stock.")
    print("Press 2: To check stock")
    print("Press 3: To enter purchase.")
    print("Press q: To quit the the program")
    return input("\nWhat would you like to do?\n")

run = menu()    # Call function by run statement

while True:
    if run == "1":      # "1": menu return input("string") -> response string too, it's not strick what we input.
        add_stock = input("\nFood Category to be added to stock?\n")
        add_food = input("\nFood to be added to stock?\n")
        amount = int(input("\nQuantity of food to be added to stock: "))
        
        add_category = get_category(add_stock.lower())
        
        if add_category in stock:
            if add_food.lower() in add_category[add_stock.lower()]:
                add_category[add_stock.lower()][add_food.lower()] += amount
            else:
                add_category[add_stock.lower()][add_food.lower()] = amount
                
            print(f"\nAdded {amount} {add_food} to {add_stock} category in stock.")
            
        else:
            stock.append({add_stock.lower(): {add_food.lower(): amount}})
            print(f"\nAdded {amount} {add_food} to {add_stock} category in stock.")
        run = menu()
        
    elif run == "2":
        print("\nCurrent stock")
        
        for category in stock:
            for key, value in category.items():
                print(f"\n{key}:")                # Category's name
                for food, amount in value.items():
                    print(f"\t{food}: {amount}")
        run = menu()
        
    elif run == "3":
        input_category = input("What kind of food was eaten?\n")
        food = input("What food was eaten?\n")
        person = input("Who ate the food?\n")
        
        category_eaten = get_category(input_category)
        category_stock = category_eaten[input_category]
            
        if food.lower() in category_stock:
            if person.capitalize() in alreadyAte:
                print("\n{} was refused and sent out of queue.".format(person.lower()))

            elif category_stock[food.lower()] > 0:
                print("\nLast stock:\n", stock)
                category_stock[food.lower()] -= 1
                print("\nCurrent stock:\n", stock)
                alreadyAte.append(person.capitalize())
                print("{} ate {}.".format(person.capitalize(), food.lower()))
                
        else:
            print("\n{} did not eat because {} out of stock.".format(person.capitalize(), food.lower()))

        run = menu()
        
    elif run.lower() == "q":
        break
    
    else:
        print("\nInvalid choice. Please follow instruction.")
        run = menu()
    
print("\nLogged out of session.")

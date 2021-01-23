import pickle
import os.path

# ask the user to select an item
# the user can:
# - "add" an item to the list
# - "show" the list of items
# - "count" to print the items count
# - "remove" the last item from the list
# - "clear" the list

# - * for the "show" command, the output should print the description, and the price also
# - * "total" to show the total to be paid
# - * "add_to_stock" ask the user for the name, description and price
# - * "stock" to list all available in stocks
# - * validate before "remove" item
# - * validate before "clear"
# - * on "show" show a message if the basket is empty
# - * save the stock in file
# - * save the basket in file


stock = {
    'cola': 5000,
    'pepsi': 10000,
    'sugar': 6000,
}

stock_description = {
    'cola': 'Coca Cola',
    'pepsi': 'Pepsi 200ml',
    'sugar': '500g'
}

basket = []

is_running = True

if os.path.exists("basket.data"):
    print("loading the basket from basket.data")
    with open("basket.data", "rb") as basket_file:
        basket = pickle.load(basket_file)

if os.path.exists("stock.data"):
    print("loading the stock from stock.data")
    with open("stock.data", "rb") as stock_file:
        stock = pickle.load(stock_file)

if os.path.exists("stock_description.data"):
    print("loading the stock from stock_description.data")
    with open("stock_description.data", "rb") as stock_description_file:
        stock_description = pickle.load(stock_description_file)


while is_running:

    command = input("Select a command (add, show, show_item, count, remove, clear, add_to_stock, stock, exit): ")

    if command == "add":
        item = input("Please enter the item name: ")

        if item in stock:
            basket.append(item)
        else:
            print(item, "does not exist in the stock!")
            print("Available items:")
            for key, price in stock.items():
                print(f"{key}: {price}")

    elif command == "show":
        if len(basket) == 0:
            print("No items in your basket.")
        else:
            for i, item in enumerate(basket):
                print(f"{i}: {item}", stock[item], stock_description[item])

    elif command == "show_item":
        index = int(input("Please enter the item index: "))
        print(basket[index])

    elif command == "count":
        print("You have", len(basket), "items.")

    elif command == "remove":
        if len(basket) > 0:
            remove_item = basket.pop()
            print("Removing last item:", remove_item)
        else:
            print("Basket already empty")

    elif command == "clear":
        if len(basket) > 0:
            basket.clear()
            print("Basket is empty now")
        else:
            print("Basket already empty")

    elif command == "total":
        total = 0
        for item in basket:
            price = stock[item]
            total = price + total

        print("The total is:", total)

    elif command == "add_to_stock":
        name = input("Enter the name: ")
        description = input("Enter the description: ")
        price = float(input("Enter the price: "))

        stock[name] = price
        stock_description[name] = description

        print("Item", name, "is added to the stock")

    elif command == "stock":
        print("Available items:")
        for key, price in stock.items():
            print(f"{key}: {price}", stock_description[key])

    elif command == "exit":

        print("saving the basket into basket.data")
        with open("basket.data", "wb") as basket_file:
            pickle.dump(basket, basket_file)

        print("saving the stock into stock.data")
        with open("stock.data", "wb") as stock_file:
            pickle.dump(stock, stock_file)

        print("saving the stock into stock_description.data")
        with open("stock_description.data", "wb") as stock_description_file:
            pickle.dump(stock_description, stock_description_file)

        print("Bye bye!")
        is_running = False

    else:
        print("Unknown command", command)

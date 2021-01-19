# ask the user to select an item
# the user can:
# - "add" an item to the list
# - "show" the list of items
# - "count" to print the items count
# - "remove" the last item from the list
# - "clear" the list

# - for the "show" command, the output should print the description, and the price also
# - "total" to show the total to be paid
# - "add_to_stock" ask the user for the name, description and price
# - "stock" to list all available in stocks
# - validate before "remove" item
# - validate before "clear"
# - on "show" show a message if the basket is empty



stock = {
    'cola': 5000,
    'pepsi': 10000,
    'sugar': 6000,
}

basket = []

is_running = True

while is_running:

    command = input("Select a command (add, show, show_item, count, remove, clear, exit): ")

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
        for i, item in enumerate(basket):
            print(f"{i}: {item}")

    elif command == "show_item":
        index = int(input("Please enter the item index: "))
        print(basket[index])

    elif command == "count":
        print("You have", len(basket), "items.")

    elif command == "remove":
        remove_item = basket.pop()
        print("Removing last item:", remove_item)

    elif command == "clear":
        print("Basket cleared.")
        basket.clear()

    elif command == "exit":
        print("Bye bye!")
        is_running = False

    else:
        print("Unknown command", command)



# web
# python,db,api,deployment -> backend: BackEnd Developer -> analysis skills, logic skills, brain, machine learning, AI
# html,js,css,ui -> frontend: FrontEnd Developer -> creativity, painting, artistic
# FullStack Developers: frontend + backend

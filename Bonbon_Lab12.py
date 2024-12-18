# Function to display the menu with prices
def display_menu():
    print("Welcome to the Food Ordering System!")
    print("Here is our menu:")
    menu = {
        "Pizza": 12.99,
        "Burger": 8.99,
        "Pasta": 10.99,
        "Salad": 5.99,
        "Soda": 2.49
    }
    for item, price in menu.items():
        print(f"{item}: ${price:.2f}")
    return menu

# Function to take the order from the user
def take_order(menu):
    while True:
        order_item = input("Please select an item from the menu: ").capitalize()
        if order_item in menu:
            print(f"You have selected {order_item}, which costs ${menu[order_item]:.2f}.")
            return menu[order_item]
        else:
            print("Invalid selection. Please choose an item from the menu.")

# Function to process payment
def process_payment(total_cost):
    while True:
        try:
            cash_rendered = float(input(f"The total cost is ${total_cost:.2f}. Please enter the cash rendered: $"))
            if cash_rendered < total_cost:
                print("Insufficient payment. Please provide enough cash.")
            else:
                change = cash_rendered - total_cost
                print(f"Payment successful! Your change is ${change:.2f}.")
                break
        except ValueError:
            print("Invalid input. Please enter a valid amount of cash.")

# Main function to orchestrate the food ordering system
def food_ordering_system():
    # Display menu
    menu = display_menu()

    # Take order
    total_cost = take_order(menu)

    # Process payment
    process_payment(total_cost)

# Run the program
if __name__ == "__main__":
    food_ordering_system()

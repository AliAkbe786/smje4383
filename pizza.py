# Function to display the menu
def display_menu():
    """
    Displays the pizza menu with prices.
    """
    menu = {
        'Margherita': 25,
        'Pepperoni': 30,
        'BBQ Chicken': 35,
        'Veggie': 20,
        'Hawaiian': 28
    }
    print("\nPizza Menu:")
    for pizza, price in menu.items():
        print(f"{pizza}: RM {price}")
    return menu

# Function to apply discounts based on order total and customer type
def apply_discount(total, is_regular):
    """
    Applies discounts to the total cost:
    - 15% discount if the total exceeds RM 100.
    - 10% discount for regular customers if total is RM 100 or less.
    """
    discount = 0
    if total > 100:
        discount = total * 0.15  # 15% discount
    elif is_regular:
        discount = total * 0.10  # 10% discount for regular customers
    return total - discount, discount

# Function to take orders from the customer
def take_order(menu):
    """
    Takes orders from the customer and calculates the total cost.
    """
    total_cost = 0
    orders = []
    
    while True:
        order = input("\nEnter the pizza you want to order (type 'done' to finish): ").strip()
        if order.lower() == 'done':
            break
        if order in menu:
            orders.append(order)
            total_cost += menu[order]
            print(f"{order} added to your order. Current total: RM {total_cost}")
        else:
            print("Sorry, this pizza is not in our menu")
    
    return orders, total_cost

# Main function to run the pizza ordering system
def pizza_ordering_system():
    """
    Main function to manage the pizza ordering system.
    """
    print("Welcome to the Pizza Ordering System!")
    menu = display_menu()  # Display the menu to the user
    
    # Take orders
    orders, total_cost = take_order(menu)
    
    if not orders:
        print("No pizzas ordered. Thank you for visiting!")
        return
    
    # Ask if the customer is a regular customer
    is_regular = input("\nAre you a regular customer? (yes/no): ").strip().lower() == 'yes'
    
    # Calculate the final cost with discounts
    final_cost, discount = apply_discount(total_cost, is_regular)
    
    # Print the order summary
    print("\nOrder Summary:")
    print(f"Pizzas ordered: {', '.join(orders)}")
    print(f"Total cost: RM {total_cost:.2f}")
    if discount > 0:
        print(f"Discount applied: RM {discount:.2f}")
    print(f"Final cost: RM {final_cost:.2f}")
    print("\nThank you for your order!")

# Run the pizza ordering system
if __name__ == "__main__":
    pizza_ordering_system()

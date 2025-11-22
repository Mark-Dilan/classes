# Define Subsystem Components
class Kitchen:
    """Represents the kitchen, responsible for preparing food orders."""
    def prepare_order(self, items):
        """Prints a message indicating the kitchen is preparing the given items."""
        print(f"Kitchen: Preparing order for: {', '.join(items)}")

class Inventory:
    """Represents the inventory, managing stock levels of food items."""
    def __init__(self):
        """Initializes the inventory with some initial stock."""
        # Using a dictionary where keys are item names and values are quantities
        self._stock = {"burger": 10, "fries": 20, "soda": 15}
        print("Inventory initialized.")

    def check_stock(self, item, quantity):
        """Checks if there is enough quantity of an item in stock."""
        if item in self._stock and self._stock[item] >= quantity:
            print(f"Inventory: Stock check for {item} (quantity {quantity}): Sufficient.")
            return True
        else:
            print(f"Inventory: Stock check for {item} (quantity {quantity}): Insufficient or item not found.")
            return False

    def deduct_stock(self, item, quantity):
        """Deducts the specified quantity of an item from the stock if available."""
        if self.check_stock(item, quantity): # Use check_stock to ensure availability before deducting
            self._stock[item] -= quantity
            print(f"Inventory: Deducted {quantity} of {item}. Remaining stock: {self._stock[item]}")
        else:
            print(f"Inventory: Cannot deduct {quantity} of {item} due to insufficient stock.")

class PaymentProcessor:
    """Represents the payment processor, handling payment transactions."""
    def process_payment(self, amount):
        """Prints a message indicating that a payment is being processed."""
        print(f"PaymentProcessor: Processing payment of ${amount:.2f}")
        # In a real system, this would involve interacting with a payment gateway.
        # For this example, we'll assume processing is always successful here.


# Define the Facade
class FoodOrderingFacade:
    """
    The Facade class for the food ordering system.
    Provides a simplified interface to the complex subsystem (Kitchen, Inventory, PaymentProcessor).
    """
    def __init__(self):
        """Initializes the Facade and creates instances of the subsystem classes."""
        print("FoodOrderingFacade: Initializing facade...")
        self._kitchen = Kitchen()
        self._inventory = Inventory()
        self._payment_processor = PaymentProcessor()
        print("FoodOrderingFacade: Facade initialized.")

    def place_order(self, order_details, payment_amount):
        """
        Places a food order by interacting with the subsystem components.
        This is the simplified method exposed to the client.

        Args:
            order_details (dict): A dictionary of items and their quantities (e.g., {'burger': 1, 'fries': 2}).
            payment_amount (float): The amount of money paid for the order.
        """
        print("\nFoodOrderingFacade: Placing order...")

        if not order_details:
            print("Order failed: No items in the order.")
            return

        # 1. Check stock for all items in the order
        print("FoodOrderingFacade: Checking stock...")
        for item, quantity in order_details.items():
            if not self._inventory.check_stock(item, quantity):
                print(f"Order failed: Insufficient stock for {item}.")
                return # Exit if stock is insufficient for any item

        # 2. Process payment if all items are in stock
        print("FoodOrderingFacade: Stock sufficient. Processing payment...")
        # In a real system, you might compare payment_amount with the calculated order total.
        # For this example, we just call the process_payment method.
        self._payment_processor.process_payment(payment_amount)
        # For this example, we assume payment is always successful after calling process_payment.
        print("FoodOrderingFacade: Payment processed successfully.")

        # 3. Deduct stock after successful payment
        print("FoodOrderingFacade: Deducting stock...")
        for item, quantity in order_details.items():
            self._inventory.deduct_stock(item, quantity)

        # 4. Prepare the order in the kitchen
        print("FoodOrderingFacade: Stock deducted. Preparing order...")
        items_list = list(order_details.keys()) # Get a list of item names to pass to the kitchen
        self._kitchen.prepare_order(items_list)

        # 5. Print a success message
        print("\nFoodOrderingFacade: Order placed successfully!")


# Add a dictionary for item prices for calculation
item_prices = {
    "burger": 5.00,
    "fries": 2.50,
    "soda": 1.50
}


# Command-line interface function
def run_ordering_interface():
    facade = FoodOrderingFacade() # Create an instance of the Facade

    print("\n--- Food Ordering System ---")

    while True:
        print("\nMenu:")
        print("1. Place Order")
        print("2. Exit")

        choice = input("Enter your choice (1-2): ")

        if choice == '1':
            order_details = {}
            total_price = 0.0

            print("\nEnter your order (enter 'done' when finished):")
            while True:
                item_name = input("Enter item name (e.g., burger, fries, soda) or 'done': ").strip().lower()
                if item_name == 'done':
                    break

                if item_name not in item_prices:
                    print(f"'{item_name}' is not a recognized item. Available items: {', '.join(item_prices.keys())}. Please try again.")
                    continue

                while True:
                    try:
                        quantity_input = input(f"Enter quantity for {item_name}: ").strip()
                        quantity = int(quantity_input)
                        if quantity <= 0:
                            print("Quantity must be a positive integer.")
                            continue
                        break
                    except ValueError:
                        print("Invalid input. Please enter a whole number for quantity.")

                order_details[item_name] = order_details.get(item_name, 0) + quantity
                total_price += item_prices[item_name] * quantity
                print(f"Added {quantity} x {item_name}. Current item total: ${item_prices[item_name] * quantity:.2f}. Order total: ${total_price:.2f}")


            if not order_details:
                print("No items added to the order.")
                continue

            print(f"\nYour final order total is: ${total_price:.2f}")

            # Place the order using the facade, passing the calculated total price
            facade.place_order(order_details, total_price)


        elif choice == '2':
            print("Exiting Food Ordering System. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 2.")

if __name__ == "__main__":
    run_ordering_interface()
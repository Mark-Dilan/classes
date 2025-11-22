class Kitchen:
    def prepare_order(self, items):
        print(f"Kitchen: Preparing order for: {', '.join(items)}")

class Inventory:
    def __init__(self):
        self._stock = {"burger": 10, "fries": 20, "soda": 15}
        print("Inventory initialized.")

    def check_stock(self, item, quantity):
        if item in self._stock and self._stock[item] >= quantity:
            print(f"Inventory: Stock check for {item} (quantity {quantity}): Sufficient.")
            return True
        else:
            print(f"Inventory: Stock check for {item} (quantity {quantity}): Insufficient or item not found.")
            return False

    def deduct_stock(self, item, quantity):
        if self.check_stock(item, quantity): 
            self._stock[item] -= quantity
            print(f"Inventory: Deducted {quantity} of {item}. Remaining stock: {self._stock[item]}")
        else:
            print(f"Inventory: Cannot deduct {quantity} of {item} due to insufficient stock.")

class PaymentProcessor:
    def process_payment(self, amount):
        """Prints a message indicating that a payment is being processed."""
        print(f"PaymentProcessor: Processing payment of ${amount:.2f}")
        
        
class FoodOrderingFacade:
    def __init__(self):
        print("FoodOrderingFacade: Initializing facade...")
        self._kitchen = Kitchen()
        self._inventory = Inventory()
        self._payment_processor = PaymentProcessor()
        print("FoodOrderingFacade: Facade initialized.")

    def place_order(self, order_details, payment_amount):
        print("\nFoodOrderingFacade: Placing order...")

        if not order_details:
            print("Order failed: No items in the order.")
            return

        
        print("FoodOrderingFacade: Checking stock...")
        for item, quantity in order_details.items():
            if not self._inventory.check_stock(item, quantity):
                print(f"Order failed: Insufficient stock for {item}.")
                return 
        print("FoodOrderingFacade: Stock sufficient. Processing payment...")

        self._payment_processor.process_payment(payment_amount)
        print("FoodOrderingFacade: Payment processed successfully.")

        print("FoodOrderingFacade: Deducting stock...")
        for item, quantity in order_details.items():
            self._inventory.deduct_stock(item, quantity)

        print("FoodOrderingFacade: Stock deducted. Preparing order...")
        items_list = list(order_details.keys()) 
        self._kitchen.prepare_order(items_list)

        print("\nFoodOrderingFacade: Order placed successfully!")


item_prices = {
    "burger": 5.00,
    "fries": 2.50,
    "soda": 1.50
}


def run_ordering_interface():
    facade = FoodOrderingFacade()

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

            facade.place_order(order_details, total_price)


        elif choice == '2':
            print("Exiting Food Ordering System. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 2.")

if __name__ == "__main__":
    run_ordering_interface()
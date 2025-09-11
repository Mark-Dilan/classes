def run_ordering_interface():
    facade = FoodOrderingFacade()

    print("\n--- Food Ordering System ---")

    while True:
        print("\nMenu:")
        print("1. Place Order")
        print("2. Exit")

        choice = input("Enter your choice (1-2): ")

        if choice == '1':
            order_details_input = input("Enter items and quantities (e.g., 'burger:1,fries:2'): ")
            payment_amount_input = input("Enter payment amount (e.g., '10.50'): ")

            order_details = {}
            try:
                items = order_details_input.split(',')
                for item_quantity_pair in items:
                    item, quantity_str = item_quantity_pair.split(':')
                    order_details[item.strip().lower()] = int(quantity_str.strip())

                payment_amount = float(payment_amount_input)

                facade.place_order(order_details, payment_amount)

            except ValueError:
                print("Invalid input format. Please use 'item:quantity,item:quantity' for order and a number for payment.")
            except Exception as e:
                print(f"An unexpected error occurred: {e}")


        elif choice == '2':
            print("Exiting Food Ordering System. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 2.")

if __name__ == "__main__":
    run_ordering_interface()
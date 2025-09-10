import abc
class RiceProduct(abc.ABC):
    @abc.abstractmethod
    def display_info(self):
        pass

    @abc.abstractmethod
    def get_type(self):
        pass

    @abc.abstractmethod
    def get_quantity(self):
        pass

    @abc.abstractmethod
    def get_quality(self):
        pass

# Concrete Classes for Specific Rice Types
class BasmatiRice(RiceProduct):
    
    def __init__(self, quantity, quality):
        self.rice_type = 'Basmati'
        self.quantity = quantity
        self.quality = quality

    def display_info(self):
        print(f"Rice Type: {self.rice_type}, Quantity: {self.quantity} kg, Quality: {self.quality}")

    def get_type(self):
        return self.rice_type

    def get_quantity(self):
        return self.quantity

    def get_quality(self):
        return self.quality

class JasmineRice(RiceProduct):
    def __init__(self, quantity, quality):
        self.rice_type = 'Jasmine'
        self.quantity = quantity
        self.quality = quality

    def display_info(self):
        print(f"Rice Type: {self.rice_type}, Quantity: {self.quantity} kg, Quality: {self.quality}")

    def get_type(self):
        return self.rice_type

    def get_quantity(self):
        return self.quantity

    def get_quality(self):
        return self.quality

class BrownRice(RiceProduct):
    def __init__(self, quantity, quality):
        self.rice_type = 'Brown'
        self.quantity = quantity
        self.quality = quality

    def display_info(self):
        print(f"Rice Type: {self.rice_type}, Quantity: {self.quantity} kg, Quality: {self.quality}")

    def get_type(self):
        return self.rice_type

    def get_quantity(self):
        return self.quantity

    def get_quality(self):
        return self.quality

# Abstract Factory Class
class RiceFactory(abc.ABC):
    """
    Abstract Factory class for creating different types of RiceProduct objects.
    Defines the interface for the factory method.
    """
    @abc.abstractmethod
    def create_rice(self, quantity, quality):
        """
        Abstract method to create a RiceProduct object.
        Concrete factories must implement this method to create specific rice types.
        """
        pass

# Concrete Factory Classes
class BasmatiRiceFactory(RiceFactory):
    def create_rice(self, quantity, quality):
        return BasmatiRice(quantity, quality)

class JasmineRiceFactory(RiceFactory):
    def create_rice(self, quantity, quality):
        return JasmineRice(quantity, quality)

class BrownRiceFactory(RiceFactory):
    def create_rice(self, quantity, quality):
        return BrownRice(quantity, quality)

# Warehouse Class to manage inventory
class Warehouse:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Warehouse, cls).__new__(cls)
            cls._instance.inventory = {} 
        return cls._instance


    def add_rice(self, factory: RiceFactory, quantity: int, quality: str):
        if not isinstance(factory, RiceFactory):
            raise ValueError("Invalid factory provided. Must be a RiceFactory instance.")
        if not isinstance(quantity, int) or quantity <= 0:
             raise ValueError("Quantity must be a positive integer.")
        if not isinstance(quality, str) or not quality:
             raise ValueError("Quality must be a non-empty string.")


        rice_product = factory.create_rice(quantity, quality)
        rice_type = rice_product.get_type()

        if rice_type not in self.inventory:
            self.inventory[rice_type] = []

        self.inventory[rice_type].append(rice_product)
        print(f"Added {quantity} kg of {quality} {rice_type} to the warehouse.")

    def display_inventory(self):
        print("\n--- Warehouse Inventory ---")
        if not self.inventory:
            print("The warehouse is empty.")
        else:
            for rice_type, products in self.inventory.items():
                print(f"Rice Type: {rice_type}")
                for i, product in enumerate(products):
                    print(f"  Product {i+1}: ", end="")
                    product.display_info()
        print("--------------------------")

# Command-line interface function
def run_warehouse_interface():
    warehouse = Warehouse() # Get the singleton instance

    # Instantiate concrete factories
    basmati_factory = BasmatiRiceFactory()
    jasmine_factory = JasmineRiceFactory()
    brown_factory = BrownRiceFactory()

    factories = {
        'basmati': basmati_factory,
        'jasmine': jasmine_factory,
        'brown': brown_factory
    }

    while True:
        print("\n--- Warehouse Menu ---")
        print("1. Add Rice")
        print("2. View Inventory")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            print("\nAvailable Rice Types: Basmati, Jasmine, Brown")
            rice_type_input = input("Enter the type of rice to add: ").lower()

            if rice_type_input in factories:
                factory = factories[rice_type_input]
                while True:
                    try:
                        quantity_input = input("Enter quantity (kg): ")
                        quantity = int(quantity_input)
                        if quantity <= 0:
                            print("Quantity must be a positive integer.")
                            continue
                        break
                    except ValueError:
                        print("Invalid input. Please enter a number for quantity.")

                quality = input("Enter quality: ")
                if not quality:
                     print("Quality cannot be empty.")
                     continue # Restart the add rice process

                try:
                    warehouse.add_rice(factory, quantity, quality)
                except ValueError as e:
                     print(f"Error adding rice: {e}")

            else:
                print("Invalid rice type.")

        elif choice == '2':
            warehouse.display_inventory()

        elif choice == '3':
            print("Exiting Warehouse Management System. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 3.")

if __name__ == "__main__":
    run_warehouse_interface()
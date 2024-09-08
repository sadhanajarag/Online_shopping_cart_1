from datetime import datetime

class ItemToPurchase:
    def __init__(self,name="none",description = "none",price=0,quantity=0):
        # Initialize the item with given name, description, price, and quantity
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
 

class ShoppingCart:
    def __init__(self,customer_name="none", current_date="January 1, 2020"):
        self.customer_name=customer_name
        self.current_date=current_date
        self.cart_item = [] # List to hold items in the cart
   
    def add_item(self,item):
        # Add an item to the cart
        self.cart_item.append(item)

    def remove_item(self,name):
        # Remove an item from the cart by name
        for item in self.cart_item:
            if item.name == name:
                self.cart_item.remove(item)
                return
        print("Item not found in cart. Nothing removed.")

    def modify_item(self,item):
         # Modify an existing item in the cart
         for i in range (len(self.cart_item)):
             if self.cart_item[i].name == item.name:
                 if item.description != "none":
                     self.cart_item[i].description = item.description
                 if item.price !=0:
                     self.cart_item[i].price = item.price
                 if item.quantity !=0:
                     self.cart_item[i].quantity = item.quantity
                     return
         print("\nItem not found in cart. Nothing modified..")           

    def print_descriptions(self):
        # Print descriptions of all items in the cart
        if not self.cart_item:
            print("SHOPPING CART IS EMPTY!!!!")
            return
        print("\t\t\t OUTPUT ITEMS' DESCRIPTIONS")
        print(f"\t\t\t{self.customer_name}'s Shopping Cart - {self.current_date}")
        print("\t\t\tItem Descriptions")
        for item in self.cart_item:
            print(f"\t\t{item.name}: {item.description}")


    def get_num_items_in_cart(self):
        # Return the total number of items (quantities) in the cart
        return sum(item.quantity for item in self.cart_item)

    def print_total(self):
        # Print the details of the cart, including total cost
        if not self.cart_item:
            print("SHOPPING CART IS EMPRY!!!")
            return
        print("\t\t\t OUTPUT SHOPPING CART ")
        print(f"\t\t{self.customer_name}'s Shopping Cart - {self.current_date}")
        print(f"\t\tNumber of Items : {self.get_num_items_in_cart()}")

        total_cost =0
        for item in self.cart_item:
            item_total = item.price * item.quantity
            total_cost += item_total
            print(f"{item.name}  {item.quantity} @ ${item.price} = ${item_total}")
        print(f"Total : ${total_cost}")

def print_menu(cart):
    #Displaying the menu and handling the choices
    while True:
        print("\n****MENU****")
        print("a - Add the item to cart")
        print("r - Remove the item from cart")
        print("c - Change the item quantity")
        print("i - Output item's description")
        print("o - Output Shopping cart")
        print("q - Quit the application")

        choice = input ("Choose the Option :").strip().lower()

        if choice == 'q':
            #Exit the Menu
            break
        if choice == 'a':
            try:
                #Add the item into the cart
                name = input("Enter the item name :")
                description = input("Enter the item description :")
                price = float(input("Enter the item price :"))
                quantity = int(input("Enter the item quantity required :"))
                item = ItemToPurchase(name,description,price,quantity)
                cart.add_item(item)

            except ValueError:
                print("Invalid input. Please enter numeric values for price and quantity.")
        
        elif choice == "r":
            # Remove an item from the cart
            name = input("Enter the name of item that you want to remove : ")
            cart.remove_item(name)


        elif choice == "c":
             # Modify an existing item in the cart
            try:
                name = input("Enter the name of item that you want to modify :")
                description_new = input("Enter the new description (or leave empty to keep unchanged): ")
                price_input = input("Enter the new price (or leave empty to keep unchanged): ")
                quantity_input = input("Enter the new quantity (or leave empty to keep unchanged): ")
                price = float(price_input) if price_input else 0
                quantity = int(quantity_input) if quantity_input else 0
                description = description_new if description_new else "none"
                item = ItemToPurchase(name,description,price,quantity)
                cart.modify_item(item)
            except ValueError:
                print("Invalid input. Please enter numeric values for price and quantity")

        elif choice == 'i':
             # Output descriptions of all items
             cart.print_descriptions()
        elif choice == 'o':
            # Output the total cost and details of the cart
            cart.print_total()
        else:
            print("Invalid choice!!! Pleasee choose the valid option...")

def get_valid_date():
    # Prompt the user to enter a valid date
    while True:
        current_date = input("Enter the current date (e.g., August 21, 2024): ")
        try:
            user_date = datetime.strptime(current_date,'%B %d, %Y').date()
            return user_date
        except ValueError:
            print("Invalid date format. Please enter a date in the format 'Month Day, Year' (e.g., August 21, 2024).")

def main():
    try:
        # Get the valid customer name
        customer_name = input("Enter the customer's name : ")
        # get the valid date
        user_date = get_valid_date()
        # for valid inputs create the shopping cart
        cart = ShoppingCart(customer_name,user_date.strftime('%B %d, %Y'))
        # Display the menu and handle user interactions
        print_menu(cart)
    except Exception as e:
        print(f"An Error Occurred : {e}")
    
if __name__ == "__main__":
    main()

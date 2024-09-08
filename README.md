Online Shopping Cart

Step 1:
Build the ItemToPurchase class with the following specifications:

Attributes
item_name (string)
item_price (float)
item_quantity (int)
Default constructor
Initializes item's name = "none", item's price = 0, item's quantity = 0
Method
print_item_cost()
Example of print_item_cost() output:
Bottled Water 10 @ $1 = $10

Step 2:
In the main section of your code, prompt the user for two items and create two objects of the ItemToPurchase class.

Example:
Item 1
Enter the item name:
Chocolate Chips
Enter the item price:
3
Enter the item quantity:
1
Item 2
Enter the item name:
Bottled Water
Enter the item price:
1
Enter the item quantity:
10

Step 3:
Add the costs of the two items together and output the total cost.

Example:
TOTAL COST
Chocolate Chips 1 @ $3 = $3
Bottled Water 10 @ $1 = $10
Total: $13
Fix any issues from milestone 1 submission prior to submitting the Portfolio Project.

From Milestone 2:
Step 4:
Build the ShoppingCart class with the following data attributes and related methods. Note: Some can be method stubs (empty methods) initially, to be completed in later steps.
Parameterized constructor, which takes the customer name and date as parameters

Attributes
customer_name (string) - Initialized in default constructor to "none"
current_date (string) - Initialized in default constructor to "January 1, 2020"
cart_items (list)
Methods
add_item()
Adds an item to cart_items list. Has parameter ItemToPurchase. Does not return anything.
remove_item()
Removes item from cart_items list. Has a string (an item's name) parameter. Does not return anything.
If item name cannot be found, output this message: Item not found in cart. Nothing removed.
modify_item()
Modifies an item's description, price, and/or quantity. Has parameter ItemToPurchase. Does not return anything.
If item can be found (by name) in cart, check if parameter has default values for description, price, and quantity. If not, modify item in cart.
If item cannot be found (by name) in cart, output this message: Item not found in cart. Nothing modified.
get_num_items_in_cart()
Returns quantity of all items in cart. Has no parameters.
get_cost_of_cart()
Determines and returns the total cost of items in cart. Has no parameters.
print_total()
Outputs total of objects in cart.
If cart is empty, output this message:
SHOPPING CART IS EMPTY
print_descriptions()
Outputs each item's description.
Example of print_total() output:
John Doe's Shopping Cart - February 1, 2020
Number of Items: 8
Nike Romaleos 2 @ $189 = $378
Chocolate Chips 5 @ $3 = $15
Powerbeats 2 Headphones 1 @ $128 = $128
Total: $521

Example of print_descriptions() output:
John Doe's Shopping Cart - February 1, 2020
Item Descriptions
Nike Romaleos: Volt color, Weightlifting shoes
Chocolate Chips: Semi-sweet
Powerbeats 2 Headphones: Bluetooth headphones

Step 5:
In the main section of your code, implement the print_menu() function. print_menu() has a ShoppingCart parameter and outputs a menu of options to manipulate the shopping cart. Each option is represented by a single character. Build and output the menu within the function.

If an invalid character is entered, continue to prompt for a valid choice. Hint: Implement Quit before implementing other options. Call print_menu() in the main() function. Continue to execute the menu until the user enters q to Quit.

Example:
MENU
a - Add item to cart
r - Remove item from cart
c - Change item quantity
i - Output items' descriptions
o - Output shopping cart
q - Quit
Choose an option:

Step 6:
Implement Output shopping cart menu option. Implement Output item's description menu option.

Example of shopping cart menu option:
OUTPUT SHOPPING CART
John Doe's Shopping Cart - February 1, 2020
Number of Items: 8
Nike Romaleos 2 @ $189 = $378
Chocolate Chips 5 @ $3 = $15
Powerbeats 2 Headphones 1 @ $128 = $128
Total: $521

Example of item description menu option.
OUTPUT ITEMS' DESCRIPTIONS
John Doe's Shopping Cart - February 1, 2020
Item Descriptions
Nike Romaleos: Volt color, Weightlifting shoes
Chocolate Chips: Semi-sweet
Powerbeats 2 Headphones: Bluetooth headphones

Fix any issues from milestone 2 submission prior to submitting the Portfolio Project.

Additional tasks for the final project submission:
Step 7:
In the main section of your code, prompt the user for a customer's name and today's date. Output the name and date. Create an object of type ShoppingCart.

Example:
Enter customer's name:
John Doe
Enter today's date:
February 1, 2020
Customer name: John Doe
Today's date: February 1, 2020

Step 8:
Implement Add item to cart menu option.

Example:
ADD ITEM TO CART
Enter the item name:
Nike Romaleos
Enter the item description:
Volt color, Weightlifting shoes
Enter the item price:
189
Enter the item quantity:
2

Step 9:
Implement remove item menu option.

Example:
REMOVE ITEM FROM CART
Enter name of item to remove:
Chocolate Chips

Step 10:
Implement Change item quantity menu option. Hint: Make new ItemToPurchase object before using ModifyItem() method.

Example:
CHANGE ITEM QUANTITY
Enter the item name:
Nike Romaleos
Enter the new quantity:
3
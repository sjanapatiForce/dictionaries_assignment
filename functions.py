# Manager to update the menu items
def update_menu_item(menu, code, field, new_value):
    # Find the item by code and update the specific field with the new value
    for item in menu:
        if item['code'] == code:
            if field in item:
                item[field] = new_value
                print(f"Updated {field} of {item['name']} to {new_value}")
                return True
            else:
                print(f"Field {field} does not exist.")
                return False
    print(f"Item {code} not found.")
    return False


def add_menu_item(menu, code, name, price, stock):
    # Add a new item to the menu
    new_item = {"code": code, "name": name, "price": int(price), "stock": int(stock)}
    menu.append(new_item)
    print(f"Added new item: {name} with code {code}, price {price}, stock {stock}")


def remove_menu_item(menu, code):
    # Remove an item from the menu based on its code
    for item in menu:
        if item['code'] == code:
            menu.remove(item)
            print(f"Removed item with code {code}: {item['name']}")
            return True
    print(f"Item {code} not found.")
    return False


# Handle customer requests and verify stock availability
def process_customer_request(menu, request_code, quantity):
    
    quantity = int(quantity)
    for item in menu:
        if item['code'] == request_code:
            if item['stock'] >= quantity:
                item['stock'] -= quantity  # Reduce the stock
                print(f"{quantity} x {item['name']} ordered. Stock remaining: {item['stock']}")
                return True
            else:
                print(f"Sorry we're left out with the stock {item['name']}. Available: {item['stock']}, Requested: {quantity}")
                return False
    print(f"Item {request_code} not found on the menu.")
    return False

# Update an existing menu item (either price or name)
def update_menu_item(menu, code, field, new_value):
    for item in menu:
        if item['code'] == code:
            if field == 'name':
                item['name'] = new_value
            elif field == 'price':
                item['price'] = int(new_value)
            print(f"{code} updated: {field} changed to {new_value}")
            return True
    print(f"Item {code} not found.")
    return False

# Add a new menu item
def add_menu_item(menu, code, name, price, stock):
    new_item = {"code": code, "name": name, "price": int(price), "stock": int(stock)}
    menu.append(new_item)
    print(f"Added new item: {new_item}")

# Removing an item from the menu
def remove_menu_item(menu, code):
    for item in menu:
        if item['code'] == code:
            menu.remove(item)
            print(f"Removed item: {code}")
            return True
    print(f"Item {code} not found.")
    return False

#taking customer requests
def take_customer_request(menu):
    request_code = input("Enter the code of the item you want to order: ").upper()
    quantity = input(f"Enter the quantity of {request_code} you want to order: ")

    if not quantity.isdigit():
        print("Invalid quantity. Please enter a number.")
        return

    quantity = int(quantity)
    
    if not process_customer_request(menu, request_code, quantity):
        print("Order could not be processed.")
    else:
        print(f"{quantity} {request_code} successfully ordered.")

#display the menu items
def display_menu(menu):
    for item in menu:
        print(f"{item['code']} - {item['name']} - ${item['price']} (stock : {item['stock']})")
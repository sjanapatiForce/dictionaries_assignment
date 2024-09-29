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
                print(f"Not enough stock for {item['name']}. Available: {item['stock']}, Requested: {quantity}")
                return False
    print(f"Item {request_code} not found on the menu.")
    return False

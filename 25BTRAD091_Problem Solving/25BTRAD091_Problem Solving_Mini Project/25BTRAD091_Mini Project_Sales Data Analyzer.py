
products = []

def add_product():
    name = input("Enter product name: ")
    quantity = int(input("Enter quantity sold: "))
    price = float(input("Enter product price: "))

    products.append({
        "name": name,
        "quantity": quantity,
        "price": price
    })

    print("Product added successfully")

def update_product():
    name = input("Enter product name: ")

    for product in products:
        if product["name"] == name:
            product["quantity"] = int(input("Enter new quantity: "))
            product["price"] = float(input("Enter new price: "))
            print("Product updated successfully")
            return

    print("Product not found")

def display_products():
    for product in products:
        revenue = product["quantity"] * product["price"]

        print("Product:", product["name"])
        print("Quantity:", product["quantity"])
        print("Price:", product["price"])
        print("Revenue:", revenue)
        print("\n")


def calculate_sales():
    total_sales = 0

    for product in products:
        revenue = product["quantity"] * product["price"]
        total_sales += revenue

    print("Total Sales:", total_sales)

    if len(products) > 0:
        highest = max(products, key=lambda p: p["quantity"])

        print("Highest Selling Product:", highest["name"])
        print("Quantity Sold:", highest["quantity"])

while True:
    print("\n1.Add Product")
    print("2.Update Product")
    print("3.Display Products")
    print("4.Calculate Sales")
    print("5.Exit")

    ch = int(input("Enter choice: "))

    if ch == 1:
        add_product()

    elif ch == 2:
        update_product()

    elif ch == 3:
        display_products()

    elif ch == 4:
        calculate_sales()

    elif ch == 5:
        print("Thank you")
        break

    else:
        print("Invalid choice")

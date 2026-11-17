
def generate_bill():
    print("       BILL GENERATOR       ")
    customer_name = input("Enter Customer Name: ")
    num_items = int(input("Enter number of item types purchased: "))
    
    total = 0.0
    items = []
    
    for i in range(1, num_items + 1):
        item_name = input(f"\nEnter name for item {i}: ")
        price = float(input(f"Enter price per unit for {item_name}: "))
        qty = int(input(f"Enter quantity for {item_name}: "))
        subtotal = price * qty
        total += subtotal
        items.append((item_name, price, qty, subtotal))
    
    tax = total * 0.05                                           # 5% tax
    grand_total = total + tax
    
    # Printing Receipt
    print("\n" + "="*40)
    print("            INVOICE RECEIPT            ")
    print("="*40)
    print(f"Customer: {customer_name}")
    print("-" * 40)
    print(f"{'Item':<15} {'Qty':<5} {'Price':<8} {'Total':<8}")
    print("-" * 40)
    for name, p, q, st in items:
        print(f"{name:<15} {q:<5} {p:<8.2f} {st:<8.2f}")
    print("-" * 40)
    print(f"Subtotal:    {total:.2f}Rs")
    print(f"Tax (5%):    {tax:.2f}Rs")
    print(f"Grand Total: {grand_total:.2f}Rs")
    print("="*40)

generate_bill()

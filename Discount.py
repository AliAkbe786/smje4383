order_amount = float(input("Enter your total pizza order amount (RM)"))

if order_amount > 100:
    discount = 0.15 * order_amount
    print(f"You get a 15% discount of RM {discount:.2f}!")
else:
    print("No discount applied. Thank you for your order")
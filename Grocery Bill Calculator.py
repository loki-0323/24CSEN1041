print("Welcome to Grocery Store 🛒")
print("Available items:")
print("1. Rice - ₹60/kg")
print("2. Sugar - ₹45/kg")
print("3. Milk - ₹50/litre")
print("4. Exit")

choice = input("Enter your choice (1-4): ")
quantity = float(input("Enter quantity (in kg/litre): "))

match choice:
    case "1":  
        price = 60 * quantity
        if quantity > 5:
            discount = price * 0.10
            price -= discount
            print(f"Discount applied: ₹{discount:.2f}")
        print(f"Total bill for Rice: ₹{price:.2f}")

    case "2":  
        price = 45 * quantity
        # 5% discount if buying more than 3kg
        if quantity > 3:
            discount = price * 0.05
            price -= discount
            print(f"Discount applied: ₹{discount:.2f}")
        print(f"Total bill for Sugar: ₹{price:.2f}")

    case "3": 
        price = 50 * quantity
        if quantity > 5:
            price -= 100
            print("Flat ₹100 discount applied!")
        print(f"Total bill for Milk: ₹{price:.2f}")

    case "4":
        print("Thank you for visiting!")

    case _:
        print("Invalid choice! Please select between 1-4.")

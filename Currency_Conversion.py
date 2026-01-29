exchange_rate = 91.93  
amount = float(input("Enter the amount: "))
print(f"1. INR to USD \n2. USD to INR")
choice = input("Choose conversion : ")

match choice:
    case "1":
        result = amount / exchange_rate
        print(f"{amount} INR = {result:.2f} USD")

    case "2":
        result = amount * exchange_rate
        print(f"{amount} USD = {result:.2f} INR")

    case _:
        print("Invalid choice! Please select either '1' or '2'.")

Output:
Enter the amount: 4132
1. INR to USD 
2. USD to INR
Choose conversion : 1
4132.0 INR = 44.95 USD

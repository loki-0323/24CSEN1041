a = int(input("Enter an integer: "))
b = int(input("Enter an integer: "))

c = a + b * 3
print(f"Value of c = {c}\n")

c = a // b * 4   
print(f"Value of c = {c}\n")

c = 3 % b * a
print(f"Value of c = {c}\n")

print("c is greater than a*b" if c > a * b else "c is not greater than a*b")

Output:
Enter an integer: 2 
Enter an integer: 4
Value of c = 14

Value of c = 0

Value of c = 6

c is not greater than a*b

a = int(input("Enter an integer (positive or negative): "))

if a > 0:
    print(f"The number {a} is positive")
elif a < 0:
    print(f"The number {a} is negative")
else:
    print(f"The number {a} is zero")

if a != 0:  # Only check even/odd if not zero
    if a % 2 == 0:
        print("The number is even")
    else:
        print("The number is odd")

Output:
Enter an integer (positive or negative): -24
The number -24 is negative
The number is even

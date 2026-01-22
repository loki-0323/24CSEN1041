a = int(input("Enter an integer as a: "))
b = int(input("Enter an integer as b: "))

# Arithmetic Operators
print("\nArithmetic Operators")
print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b:.2f}")   # Float division for clarity
print(f"{a} % {b} = {a % b}\n")

# Relational Operators
print("Relational Operators")
print(f"{a} < {b} = {a < b}")
print(f"{a} > {b} = {a > b}")
print(f"{a} == {b} = {a == b}")
print(f"{a} != {b} = {a != b}\n")

# Logical Operators
print("Logical Operators")
print(f"AND {a} and {b} = {bool(a and b)}")
print(f"OR {a} or {b} = {bool(a or b)}")
print(f"NOT {a} = {not a}\n")

# Bitwise Operators
print("Bitwise Operators")
print(f"{a} & {b} = {a & b}")
print(f"{a} | {b} = {a | b}")
print(f"Bitwise XOR {a} ^ {b} = {a ^ b}")
print(f"Left Shift {a} << 2 = {a << 2}")
print(f"Right Shift {a} >> 2 = {a >> 2}")

# Conditional (Ternary) Operator
print("\n" + ("a is greater than b" if a > b else "b is less than a"))

Output:
Enter an integer as a: 4
Enter an integer as b: 2

Arithmetic Operators
4 + 2 = 6
4 - 2 = 2
4 * 2 = 8
4 / 2 = 2.00
4 % 2 = 0

Relational Operators
4 < 2 = False
4 > 2 = True
4 == 2 = False
4 != 2 = True

Logical Operators
AND 4 and 2 = True
OR 4 or 2 = True
NOT 4 = False

Bitwise Operators
4 & 2 = 0
4 | 2 = 6
Bitwise XOR 4 ^ 2 = 6
Left Shift 4 << 2 = 16
Right Shift 4 >> 2 = 1

a is greater than b

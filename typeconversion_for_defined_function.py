def loki(n, base):
    
    if not (2 <= base <= 9):
        raise ValueError("Base must be between 2 and 9")

    if n == 0:
        return "0"

    digits = []
    while n > 0:
        digits.append(str(n % base))
        n //= base
    return ''.join(reversed(digits))

num = int(input("Enter a number: "))
base = int(input("Enter a base (2–9): "))

print(f"{num} in base {base} is: {loki(num, base)}")

Output:

Enter a number: 24
Enter a base (2–9): 4
24 in base 4 is: 120

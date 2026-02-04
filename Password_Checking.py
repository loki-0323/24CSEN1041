password = input("Enter your password: ")

errors = []

if len(password) < 8:
    errors.append("Error: Password must be at least 8 characters.")

if not any(char.isupper() for char in password):
    errors.append("Error: Password must contain at least one uppercase letter.")

if not any(char.islower() for char in password):
    errors.append("Error: Password must contain at least one lowercase letter.")

if not any(char.isdigit() for char in password):
    errors.append("Error: Password must contain at least one digit.")

if len(errors) == 0:
    print("Strong Password ")
else:
    print("Weak Password ")
    print("Errors:")
    for e in errors:
        print("-", e)

Output:
1) Enter your password: rAndom4321
Strong Password 

2) Enter your password: 12345678
ERROR!
Weak Password 
Errors:
- Error: Password must contain at least one uppercase letter.
- Error: Password must contain at least one lowercase letter.

3) Enter your password: abcdefghij
ERROR!
Weak Password 
Errors:
- Error: Password must contain at least one uppercase letter.
- Error: Password must contain at least one digit.

4) Enter your password: AbCd12
ERROR!
Weak Password 
Errors:
- Error: Password must be at least 8 characters.

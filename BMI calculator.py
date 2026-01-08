print("Body Mass Index (BMI) Calculation Program")

height = float(input("Enter height (m): "))
weight = float(input("Enter weight (kg): "))

BMI = weight / (height ** 2)

if BMI < 18.5:
    print(f"\nUnderweight BMI: {BMI:.2f}")
elif 18.5 <= BMI < 25:
    print(f"\nNormal BMI: {BMI:.2f}")
elif 25 <= BMI < 30:
    print(f"\nOverweight BMI: {index:.2f}")
else:
    print(f"\nObese BMI: {BMI:.2f}")

OUTPUT:
Enter height (m): 1.82
Enter weight (kg): 78

Normal BMI: 23.55

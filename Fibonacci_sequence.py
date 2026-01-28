n = int(input("Enter Number of Terms: "))
a, b = 0, 1
print("Fibonacci sequence: ")
for _ in range(n):
    print(a, end=" \n")
    a, b = b, a + b

Output:
Enter Number of Terms: 13
Fibonacci sequence: 
0 
1 
1 
2 
3 
5 
8 
13 
21 
34 
55 
89 
144 

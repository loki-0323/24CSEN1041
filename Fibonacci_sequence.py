n = int(input("Enter how many terms: "))
a, b = 0, 1
print("Fibonacci sequence: ")
for _ in range(n):
    print(a, end=" \n")
    a, b = b, a + b

Output:
Enter how many terms: 13
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

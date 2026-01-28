count = 0
for i in range(1, 50):
    if i % 4 == 0:   
        continue
    elif i == 15: 
        break
    else:
        pass

    print(i**2)
    count += 1

print(f"number of squares printed: {count} ")

Output:
1
4
9
25
36
49
81
100
121
169
196
number of squares printed: 11 

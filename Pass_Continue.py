count = 0
for i in range(1, 100):
    if i % 2 != 0:
        continue  
    elif i == 24:
        break    
    else:
        pass      

    print(i)
    count += 1
    
print( "the total numbers : ",count)

Output:
2
4
6
8
10
12
14
16
18
20
22
the total numbers :  11

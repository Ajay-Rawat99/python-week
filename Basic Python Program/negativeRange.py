m = int(input("enter the minimum range"))
M = int(input("enter the max range"))
for i in range(m,M+1):
    m=m+1
    if(m<0):
        print(m)
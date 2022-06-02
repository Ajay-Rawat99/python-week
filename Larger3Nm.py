a = int(input("enter first num"))
b = int(input("enter second num"))
c = int(input("enter third num"))
if(a>b & b>c):
    print("a is gretest")
elif(b>c & c>a):
    print("b is greater")
else:
    print("c is greater")
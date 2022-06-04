HIN= int(input("enter HINDI nm"))
ENG= int(input("enter ENGLISH nm"))
MATH= int(input("enter MATH nm"))
PHY= int(input("enter PHYSICS nm"))
CHE= int(input("enter CHEMISTRY nm"))
SUM = HIN+ENG+MATH+PHY+CHE
DIV= (SUM/500)*100
if HIN<33 or ENG<33 or MATH<33 or PHY<33 or CHE<33:
    print("FAILD")
elif(DIV>60):
    print("FIRST DIVISION")
elif(DIV>45):
    print("SECOND DIVISION")
elif(DIV>33):
    print("THIRD DIVISION")
else:
    print("FAILD")
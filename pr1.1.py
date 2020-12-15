import math
print("Simple calculator")
z=[]
for i in range(2):
    x = int(input("Enter the first no.:- "))
    z.append(x)
a = int(input("What opperation do you want to do? : "))
if a==1:
    b = math.fsum(z)
    print(b)
elif a==2:
    print(z[0]-z[1])
elif a==3:
    b =  print(z[0]*z[1])
    print(b)
elif a==4:
    b = math.fmod(z[0],z[1])
    print(b)
elif a==5:
    b = math.pow(z[0],z[1])
    print(b)
   

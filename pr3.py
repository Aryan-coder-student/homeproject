x = int(input("No. of items you want in list :- "))
a=[] #-> contain even integer
b=[] #-> contain negative and odd integer
for i in range(0,x):
    y=int(input("Enter the no. :- "))
    if y%2==0 and y>0 :
        a.append(y)
    else:
        b.append(y)
print("contain negative and odd integer",b)
print("contain even integer",a)

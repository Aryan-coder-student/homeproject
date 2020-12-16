import random
print("Welcome to the stone,paper,scissors game ")
x = int(input("Enter no. of people you are:-"))
a=[]
choose=["stone","paper","scissorss"]
d=[]
f=[]
t=[]
possiblities=(["stone","scissorss"],["paper","rock"],["rock","scissorss"],["scissorss","paper"])
count=0
for i in range(0,x):
    y = input("enter your name :- ")
    a.append(y)
chance = int(input("Enter no. of chance you want :-"))
for b in range(0,x):
    for n in range(0,chance):
        c = input("Enter your choice [stone,paper,scissors] :- ")
        if c not in  (choose[0] ,choose[1] , choose[2]):
            print("Enter valid a choice or get lost")
            c= input("Enter your choice [stone,paper,scissors] :- ")
            e =[random.choice(choose)]
            f.append(e)
            fl=[f[n],d[n]]
        else:
            d.append(c)
            e =[random.choice(choose)]
            f.append(e)
            type1 = f+d
            fl=[type1]
            print(e)
            if d[n]!=f[n]:
                count +=1
            else:
                count = 0
    print(a[b])
    print(d,count,"point(s)")
    print(f)
    print("=========+========= ")
    print(fl)
# WORK TO BE DONE REMOVE F LIST STORE COMPUTER CHOICE AND PLAYER CHOICES IN ONE LIST AND COMPARE IT WITH POSSIBLITIES and increase the count 




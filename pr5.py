print("Updating and sorting of numbers in a list")
a=[]
an=[] #--> ANOTHER LIST
x=int(input("enter the length of list :-"))
for i in range(0,x):
    y = int(input("Enter item :-" ))
    a.append(y)
print(a)
ask = input("Do you want to update the list(yes/no) :- ")
while ask !="yes" and ask!="no" :
    ask =input("Plz enter| Do you want to update the list(yes/no) :- ")
    break
if ask=="yes":
    ask1=input("want to remove item and add new item(y/n) :- ")
    while  ask1=="y" or ask1=="n" :
        if ask1=="y":
            ak=int(input("write the item you want to remove :-"))
            a.remove(ak)
            print(a)
            ak2=int(input("Write the element you want to add :-"))
            a.append(ak2)
            a.sort()
            print("Your final list is sorted : ",a)
        elif ask1=="n":
            ak21=input("Do you want to only delete an item ,then write(y) or only add write(n) (y/n) :- ")
            while ask1 !="y" or ask1 !="n":
                    ak21=input("Do you want to only delete an item ,then write(y) or only add write(n) (y/n) :- ")
                    if ak21=="y":
                        ak22 = int(input("write the item you want to remove :-"))
                        a.remove(ak)
                        print(a,"-->final list")
                    elif  ak21=="n":
                        ak223=int(input("write the element you want to add :- "))
                        a.append(ak223)
elif ask=="no":
    ak3=input("Want to add another list to the list(y/n) :- ")
    if ak3=="y":
        a3=int(input("Enter the lengthe of new list :- "))
        for n in range(0,a3):
            ak3 = int(input("Enter item :-" ))
            an.append(ak3)
            jl=an+a
        print(jl)
    elif ak3=="n":
        print("Thanks for using programme")
        print(a.sort(),"--->Your sorted list")







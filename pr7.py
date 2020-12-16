x = int(input("Write the no. of  entry you want : "))
cn=[]
cac=[]
cuc=[]
for i in range(0,x):
    c = input("Write the name of the Country : ")
    ca = input("Write the capital of the country : ")
    cu = input("Write the currency of the country : ")
    cn.append(c)
    cac.append(ca)
    cuc.append(cu)
print("Country","|","Capital","|","Currency")
print("------------------------------------------------")
for n in range(0,x):
    print(cn[n],"||",cac[n],"||",cuc[n])
    print("----+----+----+-----+-----+----")
s = input("Enter the country you want to search : ")
for sx in range(0,x):
    sl=cn[sx]
    if sl==s:
        print("Country","|","Capital","|","Currency")
        print("------------------------------------------------")
        print(cn[sx],"||",cac[sx],"||",cuc[sx])
    else:
        print("your country not found")
    break


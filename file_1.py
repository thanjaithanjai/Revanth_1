a=int(input("How many students?"))
b={}
for i in range(1,a+1):
    print("d of s",(i))
    rollnumber=int(input("Roll number:"))
    name = input("Name:")
    mark=float(input("Mark:"))
    c={"Roll number":rollnumber,"Name":name,"Mark":mark}
    key="a"+str(i)
    b[key]=c
print(b)

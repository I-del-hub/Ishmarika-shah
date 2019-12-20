print("enter your choice")
print("select operation")
print("1.add")
print("2.subtract")
print("3.multiply")
print("4.division")
x=int(input("enter first no."))
y=int(input("enter second no."))
c=int(input("enter your choice"))
def add(x,y):
    return(x+y)
def subtract(x,y):
    return(x-y)
def multiply(x,y):
    return(x*y)
def division(x,y):
    return(x/y)
if c==1:
   ans= add(x,y)
   print(ans)
elif c==2:
   ans=subtract(x,y)
   print(ans)
elif c==3:
   ans= multiply(x,y)
   print(ans)
elif c==4:
    ans=division(x,y)
    print(ans)
else:
    print("invalid input")
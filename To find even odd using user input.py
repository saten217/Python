x=int(input("enter a number"))
y=[]
e=[]
o=[]
d={}
def function():
    for i in range(x):
        z=int(input("input the numbers"))
        y.append(z)
function()
print(y)
def even():
    for i in y:
        if i%2==0:
            e.append(i)
even()
print(f'the even numbers are',e)
def odd():
    for i in y:
        if i%2!=0:
            o.append(i)
odd()
print(f'the odd numbers are',o)
def dic():
    d["odd"]=o
    d["even"]=e
dic()
print(d)

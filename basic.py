#this is comment
print("Hello world!")
x=5
y="john"
print(x)
print(y)

x="awesome"

def func():
    print( "Python is "+x)


func()
print( "Python is "+x)

a="hello world"

print(a[1])

print(a)
print(len(a))
for x in a:
    print(x)
    # print("\n")


txt="the best things in life are free"
print("free" in txt)

b="Hello world"
print(b[2:5])
b="Hello world"
print(b[:5])
b="Hello world"
print(b[2:])

age=36
txt="my name is john, and I am {}"

print(txt.format(age))

thislist=["apple","banana","cherry","orange","kiwi","melon","mango"]
# thislist.remove("apple")
# thislist.pop()
print(type(thislist))

thislist[1:3]=["blackcurrant","watermelon"]
# thislist[0]="blackcurrant"
print(thislist)


if "apple" in thislist:
    print("Apple is walking")

print(thislist[-1:])
print(thislist[2:5])
print(thislist[:4])
print(thislist[2:])

print(thislist[-4:-1])

fruis=['apple','banana','cherry','kiwi','mango']
newlist=[]

for x in fruis:
    if 'a' in x:
        newlist.append(x)

print(newlist)


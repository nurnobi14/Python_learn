x = 2
print(x==2)
print(x==3)
print(x>3)
print(x<=3)
print(x<=3 or x==3)

name = "shuvo"
age = 22

if name == "shuvos" and age == 22:
    print(name, " is ", age, "years old")
else: print("something is wrong")

# in operator :
ami = "shuvo"
if ami in ['nurnobi','shuvo','tony']:
    print("your name is either ",ami, "or", "nurnobi")

a = [1,2,3]
b = a
print(a == b)
print(a is b)

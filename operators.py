print("about operators")
number = 1+2*3/4.0
print(number)
# Reminder :
reminder  = 100%30
print(reminder.__str__()+" is reminder")
# Square :
sq = 10
print(sq**2)
print(sq**3)
# End Arithmetic operator :


# Using operators with string :

hello = "hello"+' world, '
print(hello)
lots = hello * 10
print(lots)

# Using operators with list :
On_number = [1,2,3,4]
To_number = [1,2,3,4]
al_number =On_number + To_number
print(al_number)

mn = [1,2,3] *4
print(mn)
# Exercise :
print('Exercise : ')
x = object()
y = object()
x_list =[x] *10
y_list =[y]*10
big_list = x_list + y_list

len_x = len(x_list)
len_y = len(y_list)
print(len_x)

print("list X_list contains %d objects"% len_x)
print("list Y_list contains %d objects"% len_y)

if x_list.count(x) == 10 and y_list.count(y) == 10:
     print("Almost there .....")
if big_list.count(x) == 10 and big_list.count(y) == 10:
    print("Great!")
print(True)
if x_list.count(x) == big_list.count(x):
    print(x_list.count(x))
else:"nothing"
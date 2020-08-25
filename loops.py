prime = [1,2,3,5,7]
for primes in prime:
    print(primes)

for x in range(4,8):
    print(x)

for y in range(4):
    print("here",y)

for z in range(4,11,4): # ekhane last 4 holo je: koto kore barbe "
    print(z)

# while loops":

count =0
while count <5 :
    print("count",count)
    count +=1

# brake and continue :
print("brake and continue")
count = 0
while True:
    print(count)
    count +=1
    if count >10:
        print("stoped")
        break
#continue :
print("continue :")
for s in range(10):
    if s % 2 == 0:  # if here type not then output is even number.
        continue
    print(s)

# else clause :
print("else clause :")
count = 10
while (count<10):
    print(count)
    count +=1
else:
    print("count value reached %d" % count)


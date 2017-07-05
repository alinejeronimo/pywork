import random
l1 = []
l2 = []
l3 = []
i = 0
for i in range(10):
    i+= 1
    num = random.choice(range(100))
    l1.append(num)
for i in range(10):
    i+= 10
    num = random.choice(range(100))
    l2.append(num)
for i in range(10):
    l3.append(l1[i])
    l3.append(l2[i])
print(l1)
print(l2)
print(l3)

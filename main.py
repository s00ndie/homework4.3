import random
list=[]
for i in range(random.randint(3,10)):
    list.append(random.randint(1,10))
print(list)
a= list[:1]
b= list[2:3]
c= [list[-2]]
print(a)
print(b)
print(c)
list2= a+b+c
print(list2)
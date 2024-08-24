import random
list=[]
for i in range(random.randint(3,10)):
    list.append(random.randint(0,10))
print(list)
non_zero_index=0
for i in range(len(list)):
    if list[i] !=0:
        list[non_zero_index]=list[i]
        non_zero_index+=1
for i in range(non_zero_index,len(list)):
    list[i]=0
print(list)
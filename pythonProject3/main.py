import random
list=[]
for i in range(random.randint(3,10)):
    list.append(random.randint(1,10))
print(list)
even_elements = sum(list[::2])
print(even_elements)
last_char= list[-1]
print(last_char)
print(even_elements*last_char)
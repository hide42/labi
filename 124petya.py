import numpy as np
w = {(0):0,(1):0,(2):0,(3):0,(4):0}
support={}#support
for x in range(5):
    for y in range(5):
        support[(x,y)] = 0
with open('affinity.txt') as file:
    for file_x in file:
        for x in range(0,5):
            if file_x[x*2] == "1":
                w[(x)] += 1 
            for y in range(0,5):
                if x != y:
                    if file_x[x*2] == "1" and file_x[y*2] == "1":
                        support[(x,y)] +=1
for sup in support:
    column_condition = int(str(sup)[1])+1
    support[sup]=support[sup]/c1[(column_condition)]
print("Уверенность: " + str(support))

print("5 правил с наибольшей поддержкой:")
for i in sorted(support, key=support.__getitem__,reverse=True)[:10:2]:
        print(i)
for i in sorted(support, key=support.__getitem__,reverse=True)[:5:]:
    print(i)


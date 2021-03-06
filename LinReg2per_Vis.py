
# coding: utf-8

# In[15]:



from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax1 = fig.add_subplot(111, projection = '3d')

x1 = []
x2 = []
y = []
f = open('data2.txt', 'r')
for line in f:
    t = line.split(' ')
    x1.append(float(t[0]))
    x2.append(float(t[1]))
    y.append(float(t[2]))
m =len(y)

ax1.scatter(x1, x2, y)
    
alf=0.1
e=0.000005

c0=0
c1=0
c2=0



x1_avg=sum(x1)/m
x2_avg=sum(x2)/m
x1_max=max(x1)
x1_min=min(x1)
x2_max=max(x2)
x2_min=min(x2)

y_avg=sum(y)/m
y_min=min(y)
y_max=max(y)

for i in range(0,m):
    x1[i]=(x1[i]-x1_avg)/(x1_max-x1_min)
    x2[i]=(x2[i]-x2_avg)/(x2_max-x2_min)
    
d0=0
d1=0
d2=0


def J(c0, c1, c2):
    j=0
    for i in range(0,m):
        j = j + pow((c0 + c1*x1[i] + c2*x2[i] - y[i]),2)
    j = j/(2*m)
    return j 


j0=J(c0,c1,c2)
j1=j0+1

while (abs(j0 - j1) > e):
    d0=0
    d1=0
    d2=0
    for i in range(0,m):
        d0=d0+(c0+c1*x1[i]+c2*x2[i]-y[i])
        d1=d1+(c0+c1*x1[i]+c2*x2[i]-y[i])*x1[i]
        d2=d2+(c0+c1*x1[i]+c2*x2[i]-y[i])*x2[i]
    d0=d0/m
    d1=d1/m
    d2=d2/m
    c0 = c0-alf*d0
    c1 = c1-alf*d1
    c2 = c2-alf*d2
    j0=j1
    j1=J(c0,c1,c2)

xx1, xx2 = np.meshgrid(range(int(x1_min),int(x1_max)+1), range(int(x2_min),int(x2_max)+1))

c0

yy = c0 + c1*(xx1-x1_avg)/(x1_max-x1_min)+ c2*(xx2-x2_avg)/(x2_max-x2_min)
ax1.plot_surface(xx1, xx2, yy, alpha=0.2)



plt.show()


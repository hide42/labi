
# coding: utf-8

# In[ ]:


import math, matplotlib.pyplot as plt

x1 = []
x2 = []
y = []
D = []

f = open('data4train.txt', 'r')
for line in f:
    t = line.split(' ')
    x1.append(float(t[0]))
    x2.append(float(t[1]))
    y.append(float(t[2]))

alf=0.1
e=0.000005
degree=6
lambd=0
m = len(y)
c = []


plt.axes(xlim = (-1, 1), ylim = (-1, 1))

for i in range(0, m):
    if y[i] == 1:
        plt.plot(x1[i],x2[i],'b^')
    else:
        plt.plot(x1[i],x2[i],'ro')    
    
for i in range(degree*(degree+2)+1):
    c.append(0)
    


def funcJ(degree, x1, x2):
    f=c[0] + (c[0]**2)*lambd
    for i in range(0,degree+1):
        for j in range(1,degree+1):
            f = f + c[j+i*degree]*(x1**j)*(x2**i) + (c[j+i*degree]**2)*lambd
        for j in range(1,degree+1):
            f = f + c[degree*(degree+1) + j]*(x2**j)
    return f

def funcd(degree):
    d = []
    for i in range(degree*(degree+2)+1):
        d.append(0)
    for k in range(0,m):
        h=1/(1+math.exp(-funcJ(degree, x1[k], x2[k])))
        d[0] = d[0]+(-y[i]+h)
        for i in range(0,degree+1):
            for j in range(1,degree+1):
                d[j+i*degree] = d[j+i*degree] + (-y[i]+h)*(x1[k]**j)*(x2[k]**i)
        for j in range(1,degree+1):
            d[j+i*degree] = d[j+i*degree] + (-y[i]+h)*(x2[k]**j)        
    for i in range(len(d)):
        d[i] = d[i]/m
    return d
    

def J(c):
    jj=0
    for i in range(0,m):
        h=1/(1+math.exp(-funcJ(degree, x1[i], x2[i])))  
        if h==0 or h<0:
            print("nu ti i dura")
        jj = jj + (-y[i]*math.log(h)-(1-y[i])*math.log(1-h))
    return jj/m

j0=J(c)
j1=j0+1

while (abs(j0 - j1) > e):
    D = funcd(degree)
    for i in range(len(c)):
             c[i] = c[i] - alf*D[i]
    j0=j1
    j1=J(c)
    

plt.show()



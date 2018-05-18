
# coding: utf-8

# In[11]:


x1 = []
x2 = []
y = []
f = open('data2.txt', 'r')
for line in f:
    t = line.split(' ')
    x1.append(float(t[0]))
    x2.append(float(t[1]))
    y.append(float(t[2]))

alf=0.1
e=0.000005

c0=0
c1=0
c2=0

m = len(y)

x1_avg=sum(x1)/m
x2_avg=sum(x2)/m
x1_max=max(x1)
x1_min=min(x1)
x2_max=max(x2)
x2_min=min(x2)

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


print(c0)
print(c1)
print(c2)

x11=1500
x22=3

x11=(x11-x1_avg)/(x1_max-x1_min)
x22=(x22-x2_avg)/(x2_max-x2_min)

print(c0+c1*x11+c2*x22)


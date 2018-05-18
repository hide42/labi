
import matplotlib.pyplot as plt
import matplotlib.animation as animation

x = []
y = []
f = open('1.txt', 'r')
for line in f:
    t = line.split(' ')
    x.append(float(t[0]))
    y.append(float(t[1]))

alf=0.001
e=0.000005

c0=0
c1=0

m = len(x)

d0=0
d1=0

def J(c0, c1):
    j=0
    for i in range(0,m):
        j = j + pow((c0 + c1*x[i] - y[i]),2)
    j = j/(2*m)
    return j 

j0=J(c0,c1)
j1=j0+1

h1=[1,25]
h2=[]

while (abs(j0 - j1) > e):
    d0=0
    d1=0
    for i in range(0,m):
        d0=d0+c0+c1*x[i]-y[i]
        d1=d1+(c0+c1*x[i]-y[i])*x[i]
    d0=d0/m
    d1=d1/m
    c0 = c0-alf*d0
    c1 = c1-alf*d1
    j0=j1
    j1=J(c0,c1)
    
    h2.append([c0+c1*h1[0],c0+c1*h1[1]])  

    
fig = plt.figure()
ax = plt.axes(xlim = (5,25), ylim = (-5, 25))

plt.plot(x,y, 'ro')

line, = ax.plot([], [], lw = 2)

def init():
    line.set_data([], [])
    return line,

def animate(i):
    line.set_data(h1, h2[i])
    return line,


anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=30, interval=500, blit=True)

plt.show()
   

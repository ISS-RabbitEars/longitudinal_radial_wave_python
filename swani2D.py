import math
import random
import matplotlib.pyplot as plt
from matplotlib import animation

N=10000
x0=[]
y0=[]
x=[]
y=[]

fig, a=plt.subplots()

for i in range(N+1):
	x0.append(10*(1-2*random.random()))
	y0.append(10*(1-2*random.random()))
	x.append(0)
	y.append(0)

def norm(x,y):
	return(math.sqrt(x**2+y**2))

def gamma(x,y,t):
	return(1+2*math.sin(norm(x,y)-t)/norm(x,y))

def run(frame):
	plt.clf()
	for i in range(N+1):
		x[i]=x0[i]*gamma(x0[i],y0[i],frame)
		y[i]=y0[i]*gamma(x0[i],y0[i],frame)
	plt.scatter(x,y,s=1,color='r')
	ax=plt.gca()
	ax.set_aspect(1)
	plt.xlim([-9,9])
	plt.ylim([-9,9])
	ax.set_facecolor('xkcd:black')
    
ani=animation.FuncAnimation(fig,run,interval=1)
writervideo = animation.FFMpegWriter(fps=10)
ani.save('swani2D.mp4', writer=writervideo)
plt.show()

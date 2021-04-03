import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button
from random import randint
from scipy import random
#option_3
from scipy import signal
# https://docs.scipy.org/doc/scipy/reference/tutorial/signal.html
from scipy.integrate import odeint
# import all classes/methods 
# from the tkinter module 
from tkinter import *
import matplotlib.cm as cm
import random
import math
import scipy.integrate as integrate
import scipy.special as special
class plotter:
	def __init__(self, x_points, y_points,xr,yr):
		self.x_points = x_points
		self.y_points = y_points
		self.r = []
		self.xr = xr
		self.yr = yr
		self.DATA_X = []
		self.DATA_Y = []
	def __init__(self):
		self.x_points = []
		self.y_points = []
		self.yr = []
		self.xr = []
		self.DATA_X = []
		self.DATA_Y = []
		print("init")

	def calculate_option1(self, nps, a, b, c, d, e, f, p): #fractals
		# https://alyssaq.github.io/2015/visualising-matrices-and-affine-transformations-with-python/
		# https://scipython.com/book/chapter-7-matplotlib/examples/the-barnsley-fern/
		# play around
		# a_const = [0.05,0.05,0.46,0.47,0.20,0.20]
		# b_const = [0.3,0.2,-0.15,-0.1,0.28,0.26]
		# c_const = [0.2,0.1,0.39,0.17,0.-0.25,0.0]
		# d_const = [0.60,-0.5,0.38,0.42,0.45,0.60]
		# e_const = [0.0,0.0,0.0,0.0,0.0,0.0,0.0]
		# f_const = [1,0.8,0.6,1.10,1.1,.7]
		a_const = [0.05,0.05,0.46,0.47,0.43,0.42]
		b_const = [0.00,0.00,-0.15,-0.1,0.28,0.26]
		c_const = [0.00,0.00,0.39,0.17,0.-0.25,-0.35]
		d_const = [0.60,-0.5,0.38,0.42,0.45,0.31]
		e_const = [0.0,0.0,0.0,0.0,0.0,0.0,0.0]
		f_const = [0.0,0.8,0.6,1.10,1.1,.7]
		# f2 = lambda x,y: (a_const[1]*x+b_const[1]*y+e_const[1], c_const[1]*x+d_const[1]*y+f_const[1])
		# f3 = lambda x,y: (a_const[2]*x+b_const[2]*y+e_const[2], c_const[2]*x+d_const[2]*y+f_const[2])
		# f4 = lambda x,y: (a_const[3]*x+b_const[3]*y+e_const[3], c_const[3]*x+d_const[3]*y+f_const[3])
		p = [0.01,0.85,0.07,0.07]
		q = [p[0],p[0]+p[1],p[0]+p[1]+p[2],p[0]+p[1]+p[2]+p[3]]
		# f1 = lambda x,y: (0., 0.16*y)
		# f2 = lambda x,y: (0.85*x + 0.04*y, -0.04*x + 0.85*y + 1.6)
		# f3 = lambda x,y: (0.2*x - 0.26*y, 0.23*x + 0.22*y + 1.6)
		# f4 = lambda x,y: (-0.15*x + 0.28*y, 0.26*x + 0.24*y + 0.44)
		# a_const = [0.83,0.23,0.23,0.0]
		# b_const = [0.04,-0.23,0.23,0.0]
		# c_const = [-0.04,0.23,-0.23,0.0]
		# d_const = [0.80,0.23,0.23,0.25]
		# e_const = [0.0,0.0,0.0,0.0]
		# f_const = [0.2,0.15,0.18,0.00]

		x, y = 0.5, 0.5
		for i in range(int(nps)):
			for transformation in range(4):
				ran = random.randint(0,1)
				if ran < q[transformation]:
					a = a_const[transformation]
					b = b_const[transformation]
					e =e_const[transformation]
					c =c_const[transformation]
					d =d_const[transformation]
					f =f_const[transformation]
					x= a*x+b*y+e
					y= c*x+d*y+f
					self.x_points.append(x)
					self.y_points.append(y)
					self.x_points.append(-x)
					self.y_points.append(y)					
			
			self.DATA_X.append([self.x_points])
			self.DATA_Y.append([self.y_points])

	def plot_option1(self,nps,ls='--',lw=1.2,colors=None):

		fig, ax = plt.subplots()
		plt.subplots_adjust(bottom=0.15)
		# Canvas size (pixels)
		width, height = 300, 300
		aimg = np.zeros((width, height))
		plt.scatter(self.x_points, self.y_points, s=1)
		plt.xlabel('x')
		plt.ylabel('y')

		plt.show()

		
		def update_wave(val):
			idx = int(sliderwave.val)
			ax.cla()
			ax.plot(DATA_X[idx], DATA_Y[idx], '-o')
			#  ax.set_title(f'Slide No. {idx}')
			fig.canvas.draw_idle()

		axwave = plt.axes([0.25, 0.05, 0.5, 0.03])
		sliderwave = Slider(axwave, 'Event No.', 0, 4, valinit=0, valfmt='%d')
		sliderwave.on_changed(update_wave)
		plt.show()

	def calculate_option2(self, dr, de): # Hardwall
		u = []
		g = []
		radi = [30,35,40,50]

		def V(r):
			if r in radius:
				return 0
			elif r == 0:
				return 0
			else:
				return -(1/r)

		def U(f, i):
			ufactor = (12-10*g[i])*u[i] - g[i-1]*u[i-1]
			return ufactor

		def G(f):
			gfactor = 1-((1/12)*dr*dr*f)
			return gfactor

		def E_root(n):
			return (-1/2*n*n)

		def F(r,e,l):
			f = ((l*(l+1)/r*r)+(2/(r*r))-2*e)
			return f

		espace = np.arange(-0.6,0,de) 


		for l in range(4): #calculate for each r 
			print("l number : ", l)
			if l == 0 :
			# else :
				for e in espace :
					for radius in radi:
						interval = float(radius)*dr
						r = [a + interval * i for i in range (1/dr)]
						I = 0
						for j in range(N):
							x = a + dr * j
							I = I + fn(x)*dr 

					print("		radius calculating : ", radius) 
					n=0
					r=0
					while r != radius: #calculate up to each r with dr
						if n==0:
							u.append(0)
							g.append(0)				
							r+=dr
						if n==1:
							u.append(0.01)
							f = F(l,r,e)
							gfactor = G(f)
							g.append(gfactor)
							n+=1
							r+=dr
						else:
							f = F(l,r,e)
							gfactor = G(f)
							g.append(gfactor)
							ufactor = U(f,n)/gfactor
							u.append(ufactor)
							if u[n-1] * u[n] < 0 :
								c = (l - 0.5)*dr
								if c not in self.x_points:				
									self.x_points.append(c)
									self.y_points.append(e)
									print(c,e)
							n+=1
							r+=dr
					u.clear() # only use u[] for each radius
				e += de

	def plot_option2 (self,ls='--',lw=1.2,colors=None):

		fig, ax = plt.subplots()
		plt.subplots_adjust(bottom=0.15)
		# Canvas size (pixels)
		width, height = 300, 300
		aimg = np.zeros((width, height))
		plt.scatter(self.x_points, self.y_points, s=1)
		plt.xlabel('C')
		plt.ylabel('E')
		plt.show()

	def calculate_option3 (self,npts,a,b):	
		def mc_integration(self):
			self.npts=1000
			xrand = random.uniform(a,b,self.npts)
			def func(x):
				return np.sin(x)

			integral = 0

			for i in range(N):
				integral += func(xrand[i])

			res = (b-a)/float(N)*integral

	def reset(self):
		self.x_points = []
		self.y_points = []
		self.yr = []
		self.xr = []
		self.DATA_X = []
		self.DATA_Y = []

	# def save(self):


		





# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 18:08:50 2016

@author: Administrator
"""

import numpy as np
import matplotlib.pyplot as plt

b=0.2
v0=20
mg=9.8
a1=(35.0/180)*np.pi
a2=40.0/180*np.pi
a3=45.0/180*np.pi
a4=50.0/180*np.pi
a5=55.0/180*np.pi
y=[]
x = np.linspace(0,32,1000)
y1= ((np.tan(a1))+mg/(b*v0*np.cos(a1)))*x+(mg/b**2)*np.log(1-(b*x)/(v0*np.cos(a1)))
y2= ((np.tan(a2))+mg/(b*v0*np.cos(a2)))*x+mg/b**2*np.log(1-(b*x)/(v0*np.cos(a2)))
y3= ((np.tan(a3))+mg/(b*v0*np.cos(a3)))*x+mg/b**2*np.log(1-(b*x)/(v0*np.cos(a3)))
y4= ((np.tan(a4))+mg/(b*v0*np.cos(a4)))*x+mg/b**2*np.log(1-(b*x)/(v0*np.cos(a4)))
y5= ((np.tan(a5))+mg/(b*v0*np.cos(a5)))*x+mg/b**2*np.log(1-(b*x)/(v0*np.cos(a5)))
plt.plot(x,y1,color="green",linewidth=1,linestyle='--') 
plt.plot(x,y2,color="red",linewidth=1,linestyle='--')
plt.plot(x,y3,color="yellow",linewidth=1,linestyle='--')
plt.plot(x,y4,color="blue",linewidth=1,linestyle='--')
plt.plot(x,y5,color="black",linewidth=1,linestyle='--')
plt.axis([0,max(x),0,max(y5)+2])
plt.show()

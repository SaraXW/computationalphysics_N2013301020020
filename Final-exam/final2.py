# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 18:13:49 2016

@author: Administrator
"""

import numpy as np
import matplotlib.pyplot as plt
b1=0.01
b2=0.1
b3=1.0
b4=2.0
b5=5.0
v0=20
mg=9.8
a =45.0/180*np.pi
x = np.linspace(0,40,1000)
y1= ((np.tan(a))+mg/(b1*v0*np.cos(a)))*x+(mg/b1**2)*np.log(1-(b1*x)/(v0*np.cos(a)))
y2= ((np.tan(a))+mg/(b2*v0*np.cos(a)))*x+(mg/b2**2)*np.log(1-(b2*x)/(v0*np.cos(a)))
y3= ((np.tan(a))+mg/(b3*v0*np.cos(a)))*x+(mg/b3**2)*np.log(1-(b3*x)/(v0*np.cos(a)))
y4= ((np.tan(a))+mg/(b4*v0*np.cos(a)))*x+(mg/b4**2)*np.log(1-(b4*x)/(v0*np.cos(a)))
y5= ((np.tan(a))+mg/(b5*v0*np.cos(a)))*x+(mg/b5**2)*np.log(1-(b5*x)/(v0*np.cos(a)))
plt.plot(x,y1,color="green",linewidth=1,linestyle='--') 
plt.plot(x,y2,color="red",linewidth=1,linestyle='--')
plt.plot(x,y3,color="yellow",linewidth=1,linestyle='--')
plt.plot(x,y4,color="blue",linewidth=1,linestyle='--')
plt.plot(x,y5,color="black",linewidth=1,linestyle='--')
plt.axis([0,max(x),0,max(y1)+2])
plt.show()

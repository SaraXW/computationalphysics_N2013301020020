# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 22:09:29 2016

@author: Administrator
"""

from pylab import*
v=[]
t=[]
a=10
b=1
dt=0.1
endtime=100
v.append(0)
t.append(0)
for i in range(int(endtime/dt)):
	v.append(v[i]+(a-b*v[i])*dt)
	t.append(t[i]+dt)
	print t[-1] ,v[-1]

plot(t,v,'r')
title('the velocity of a parachutist')
xlabel('t')
ylabel('v')
show()
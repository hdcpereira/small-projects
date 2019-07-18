#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np 
import matplotlib.pyplot as plt
from numpy import trapz
import glob


# In[2]:


def cross_section(Z1,Z2,Ma,Mp,Theta,K):
    
    Theta = np.deg2rad(Theta)
    
    t = ((0.72*Z1*Z2)/K)**2
    d = np.sqrt(1 -((Mp*np.sin(Theta))/Ma)**2)
    g = (np.cos(Theta) + d)**2
    f = np.sin(Theta)**4* d
         
    sigma = t*(g/f)
         
    return sigma


# In[3]:


d11 = glob.glob('*M.dat')
d21 = glob.glob('*P.dat')
d11.sort()
d21.sort()

d12 = glob.glob('*M.sra')
d12.sort()


# In[4]:


alpha = []
i = 0
for x in d12:
    with open (d12[i],'rb') as myfile:
        t = str([(x.strip()) for ei, x in enumerate(myfile) if ei in [0]])
        t = t.split(' ')
        alpha.append(t[1])
        i += 1

i = 0
datafixo = []
for x in d11:
    datafixo.append(np.loadtxt(d11[i]))
    i += 1 
    
i = 0
areafixo = []
for x in datafixo:
    areafixo.append(np.sum(datafixo[i][474:491]))
    i += 1

i = 0
datamovel = []
for x in d21:
    datamovel.append(np.loadtxt(d21[i]))
    i += 1 

i = 0
areamovel = []
for x in datamovel:
    areamovel.append(np.sum(datamovel[i][416:436]))
    i += 1


# In[5]:


areafixo.reverse()
areamovel.reverse()
alpha.reverse()


# In[56]:


dsigma = cross_section(1,79,197,1,170,2.4)
darea = np.divide(areamovel,areafixo)
constante = 1.613 * dsigma

x1 = np.arange(80,150,1)
y1 = cross_section(1,79,197,1,x1,2.4)
x2 = alpha
y2 = constante*darea


# In[60]:


plt.figure()

plt.scatter(x2,y2)
plt.scatter(x1,y1)
plt.xlabel(r'$\theta$ (graus)')
plt.ylabel(r'Seção de Choque (fm$^2$/sr)')

plt.show()



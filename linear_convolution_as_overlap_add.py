# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 11:04:07 2018

@author: cb.en.u4ece17228
"""
import numpy as np
import matplotlib.pyplot as plt
a=int(input('Enter the length of the x[n] : '))
b=int(input('Enter the length of the h[n] : '))
k=int(input('Enter the block size : '))
l=np.remainder(a,k)
if(l!=0):
    l=l+1
else :
    l=a/k
N=l+b-1
x=np.zeros(a)
h=np.zeros(N)
n1=np.arange(a)
n2=np.arange(b)
h1=np.zeros(b)
n3=np.arange(a+b-1)
for i in range(0,a):
    x[i]=input("Enter the value of x["+str(i)+"] : ")
for i in range(0,b):
    h[i]=input("Enter the value of h["+str(i)+"] : ")
for i in range (0,b):
    h1[i]=h[i]
y1=[[0 for i in range (N)]for j in range (l)]
y2=[[0 for i in range (N)]for j in range (N)]
d=[[0 for i in range (a+b-1)]for j in range (l)]
p=0
for i in range(0,l):
        for j in range(0,k):
            if(p<a):
                y1[i][j]=x[p]
            p=p+1
for i in range(0,l):
    for j in range (0,N):
        if(j==0):
            y2[j]=y1[i]
        else:
            y2[j]=np.roll(y2[j-1],1)
        if (j==(N-1)):
            y2=np.transpose(y2)
            for q in range(0,N):
                d[i][q]=sum(y2[q]*h)
for i in range(0,l):
    for j in range(0,i*b):
        d[i].insert(0,0)
s=np.zeros(a+b-1)
s1=np.zeros(a+b-1)
for i in range(0,a+b-1):
    for j in range(0,l):
        s[i] +=d[j][i]
print ('Using over lap method : ')
print s
s1=np.convolve(x,h1)
print('Using linear  convolution : ')
print s1
plt.subplot(4,1,1)
plt.stem(n1,x)
plt.xlabel('Index n')
plt.ylabel('Amplitude')
plt.title('Input signal x[n]')
plt.subplot(4,1,2)
plt.stem(n2,h1)
plt.xlabel('Index n')
plt.ylabel('Amplitude')      
plt.title('h[n]')
plt.subplot(4,1,3)
plt.stem(n3,s)
plt.xlabel('Index n')
plt.ylabel('Amplitude')
plt.title('Using overlap add method ')
plt.subplot(4,1,4)
plt.stem(n3,s1)
plt.xlabel('Index n')
plt.ylabel('Amplitude')
plt.title('Using linear convolution method ')
plt.show()
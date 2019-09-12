#!/usr/bin/env python
# coding: utf-8

# In[ ]:


a=[1,2,3,4,5]  #an array
l=list()
k=0
n=1
g=len(a)
for i in a:
    k=sum(a[0:n])-sum(a[n:g])   #geting difference in their sums
    n+=1
    k=abs(k)                   #positive value
    l.append(k)
    k=min(l)                   #mean value
    
print(k)
    


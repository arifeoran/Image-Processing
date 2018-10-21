#!/usr/bin/env python
# coding: utf-8

# In[12]:


liste=[0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1]
for i in liste:
    print(int(i)+1)

for i in range(0,len(liste)):
    liste[i]=liste[i]+1
print(liste)


# In[13]:


import random
s=random.randint(2,5)
print(s)


# In[14]:


listee=[]
for i in range(10):
    listee.append(random.randint(0,10))
print(listee)


# In[15]:


test_sayisi=100000
def createArray(s):
    myList=[]
    for i in range(s):
        myList.append(random.randint(0,10))
    return myList


# In[16]:


def printArray(array):
    print(array)


# In[18]:


def incArray(array):
    myList_1=[]
    for i in array:
        myList_.append(i+1)
    return myList_1


# In[20]:


def createArrayVersion(s):
    myList=np.arrange(s):
        return myList


# In[23]:


dizi_1=createArray(test_sayısı)
printArray(dizi_1)
dizi_2=incArray(dizi_1)
printArray(dizi_2)


# In[25]:


import numpy as np
x=np.arange(10)
x


# In[26]:


myL=createArrayVersion(test_sayısı)
myL=myL+25
myL[10025]


# In[ ]:


import matplotlib.pyplot as plt
image_1=plt.imread("test_1.jpg")
plt.imshow(image_1)
plt.show()
image_1.shape
type(image_)


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# In[1]:


### soru1
### a) 28x28 lik içeriği 0 ve1 olan bir matris return eden fonksiyon yazınız 
### b) a a-da elde dilen matris içerisinde 1 leri içeren MBR i return eden fonksiyonu yazınız
### c)28x28 lik iki vektörün bezerliğini return eden fonksiyon
### d) a şıkkında yazdığınız fonksiyonu kullanarak 100 farklı matris elde edip birinci üretilen ile diğerlerini karşılaştırıp yakınlığını benzerliğini listeleyiniz


# In[ ]:


import numpy as np
import matplotlib.pyplot as plt
import random as random


# In[12]:


### soru1 
## a nın cevabı
def matris_create_28_by_28_with_0_1():
    my_matris=np.zeros((28,28))
    for i in range(28):
        for j in range(28):
            my_matris[i,j]=random.randint(0,1)
    return my_matris
## soru 1 b nin cevabı
def MBR_create_28_by_28_with_0_1(matris_a):
    m=matris_a.shape[0]
    n=matris_a.shape[1]
    x_min=m
    x_max=0    #başlangıç değeri olası en olumsuz durum
    y_min=n
    y_max=0
    for i in range(m):
        for j in range(n):
            if (matris_a[i,j]==1 and x_min>i):      #resim matris üzerinden 
                x_min=i                            #x_min,.... güncelleniyor
            if (matris_a[i,j]==1 and x_max>i):
                x_max=i
            if (matris_a[i,j]==1 and y_min>j):
                y_min=j
            if (matris_a[i,j]==1 and y_max<j):
                y_max=j    
    return (x_min,x_max,y_min,y_max)

### soru 1 c nin cevabı
def get_similarity(character_a,character_b):
    m=character_a.shape[0]
    n=character_a.shape[1]
    my_similarity=0
    for i in range(m):
        for j in range(n):
            my_similarity=my_similarity + character_a[i,j]*character_b[i,j]
    return my_similarity
## soru 1 dnin cevabı
def get_similarity_for_100_characters(kac_karakter=100):
    characters=[]
    for i in range(kac_karakter):
        new_char=matris_create_28_by_28_with_0_1()
        characters.append(new_char)
    for i in range(kac_karakter):
        benzerlik=get_similarity(characters[0],characters[1])
        print("0 --"+ str(i) + " " ,benzerlik)
    


# In[8]:


c_1=matris_create_28_by_28_with_0_1() #m, MBR_create_28_by_28_with_0_1(m)
c_2=matris_create_28_by_28_with_0_1()
get_similarity(c_1,c_2)
get_similarity_for_100_characters(10)


# In[ ]:





# In[ ]:





# In[ ]:





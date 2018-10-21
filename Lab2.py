#!/usr/bin/env python
# coding: utf-8




import matplotlib.pyplot as plt
import matplotlib.image as mpimg
img_mpinmg.imread('test1.jpg')
#%matplotlib inline
import numpy as np





im_1=plt.imread("image_1.jpg")
plt.imshow(im_1)
plt.show()





def fonk(image_1):
    print("Resim boyutu :",image_1.ndim,"\n")
    print("Resim shape değeri :",image_1.shape,"\n")
    print("Red için minimum değer :", image_1[:,:,0].min(),"\n")
    print("Red için maksimum değer : ", image_1[:,:,0].max(),"\n")





fonk(image_1)
im_1[:,:,0]=im_1[:,:,0]+50
plt.imshow(im_1)
plt.show()





def my_function(image_2):
    print("Eksen sayısı :",image_2.ndim)
    print("Eksen değerleri :", image_2.shape)
    print("En küçük kırmızı renk değeri :" , np.min(image_2[:,:,0]))
    print("En büyük kırmızı renk değeri :", np.max(image_2[:,:,0]))
    print("En küçük yeşil renk değeri :" , np.min(image_2[:,:,0]))
    print("En büyük yeşil renk değeri : ", np.max(image_2[:,:,0]))
    print("En küçük mavi renk değeri :" , np.min(image_2[:,:,0]))
    print("En büyük mavi renk değeri :" , np.max(image_2[:,:,0]))




my_function(im_1)


import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage.filters import rank

from BoxcarZeroPadding import BoxcarZeroPadding

k_size=35;
input_image =cv2.imread('characterTestPattern688.tif')[:,:,1]
output_image=BoxcarZeroPadding(input_image,k_size);

imgs=[input_image,output_image]

k, axes =plt.subplots(1,2,figsize=(10,10))
ax=axes.ravel()
tuple ='output: k='+str(k_size)
titles=['input: Original',tuple]
for n in range(0, len(imgs)):
    ax[n].imshow(imgs[n],cmap=plt.cm.gray)
    ax[n].set_title(titles[n])
    ax[n].axis('off')

plt.tight_layout()
plt.show()

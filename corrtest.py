import numpy as np
from scipy.ndimage import correlate

H=np.mat([[1,2,1],[2,4,2],[1,2,1]]);
I=np.mat([[1,5,9,13],[2,6,10,14],[3,7,11,15],[4,8,12,16]]);
print('I =')
print(I)
print('H =')
print(H)
output=correlate(I, H, mode='constant',cval=0.0);
print('output =')
print(output)

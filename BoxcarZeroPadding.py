import numpy as np
from scipy.ndimage import correlate
def BoxcarZeroPadding(image,k):
    # print(image.shape)
    boxcar_filter=np.ones((k,k))/(k*k);
    output = correlate(image, boxcar_filter, mode='constant', cval=0.0);
    return output;
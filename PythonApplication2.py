from skimage import data,io,filter,color
from skimage.segmentation import slic
import numpy as np
import matplotlib.pyplot as plt

li = np.zeros((100,100,100))
for z in range(0,100):
    for y in range(0,100):
        for x in range(0,100):
            li[x,y,z] = (x-50)**2 + (y-50)**2 + (z-50)**2
vox = li
print np.shape(vox)
segments = slic(vox,n_segments = 300,compactness = 30,multichannel = False)
print segments
plt.subplot(121)
plt.imshow(segments[20])
plt.subplot(122)
plt.imshow(segments[50])
plt.show()

#img = io.imread('PriPara.bmp')

#segments = slic(img,n_segments = 300,compactness = 30,convert2lab = True,multichannel = True)
#out1 = color.label2rgb(segments, img, kind='avg')

#plt.subplot(121)
#plt.imshow(img)
#plt.subplot(122)
#plt.imshow(out1, interpolation='nearest')
#plt.show()
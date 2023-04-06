import matplotlib.pyplot as plt

from skimage import data
from skimage.io import imread
from skimage.color import rgb2gray
from skimage.filters import threshold_otsu
from skimage.filters import threshold_minimum
from skimage.filters import threshold_mean

img = data.camera()
trshmin = threshold_minimum(img)
print("Threshold Minimum: ", trshmin)
minimg = img > trshmin

trshmean = threshold_mean(img)
print("Threshold Mean: ", trshmean)
meanimg = img > trshmean

fig, axes = plt.subplots(3,2, figsize=(5,5))
ax = axes.ravel()

ax[0].imshow(img, cmap=plt.cm.gray)
ax[0].set_title("original")
ax[1].hist(img.ravel(), bins=256)
ax[1].set_title("Histogram Image")
ax[2].imshow(minimg, cmap=plt.cm.gray)
ax[2].set_title("Threshold Minimum")
ax[3].hist(img.ravel(), bins=256)
ax[3].set_title("Histogram Minimum")
ax[4].imshow(meanimg, cmap=plt.cm.gray)
ax[4].set_title("Threshold Mean")
ax[5].hist(img.ravel(), bins=256)
ax[5].set_title("Histogram Mean")

plt.tight_layout()
plt.show()


import matplotlib.pyplot as plt

from skimage import data
from skimage.io import imread
from skimage.color import rgb2gray

ori = data.coffee()
print(ori.shape)

plt.imshow(ori)
#plt.show()

red = ori[:, :, 0]
green = ori[:, :, 1]
blue = ori[:, :, 2]

print(" red shape: ", red.shape)
print(" green shape: ", green.shape)
print(" blue shape: ", blue.shape)

fig, axes = plt.subplots(2,2, figsize=(8,8))
ax = axes.ravel()

ax[0].imshow(ori)
ax[0].set_title("Citra Input")
ax[1].imshow(red, cmap= plt.cm.gray)
ax[1].set_title("Red Channel")
ax[2].imshow(green, cmap=plt.cm.gray)
ax[2].set_title("Green Channel")
ax[3].imshow(blue, cmap=plt.cm.gray)
ax[3].set_title("Blue Channel")

fig.tight_layout()

red = ori.copy()
red[:, :, 1] = 0
red[:, :, 2] = 0

green = ori.copy()
green[:, :, 0] = 0
green[:, :, 2] = 0

blue = ori.copy()
blue[:, :, 0] = 0
blue[:, :, 1] = 0

fig, axes = plt.subplots(2,2, figsize=(8,8))
ax = axes.ravel()

ax[0].imshow(ori)
ax[0].set_title("Citra Input")
ax[1].imshow(red)
ax[1].set_title("Red Channel")
ax[2].imshow(green)
ax[2].set_title("Green Channel")
ax[3].imshow(blue)
ax[3].set_title("Blue Channel")

fig.tight_layout()
plt.show()

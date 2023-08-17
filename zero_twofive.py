import rasterio
from rasterio import show
from matplotlib import pyplot as plt

img = rasterio.open('E:\Only-CO-Lang\Python Code\CODE-py\Flood Ai\mine\srm\band03_srm.tif')
show(img)

full_img=img.read()

num_band=img.count
print('Number fo bands in the image =',num_band)

img_band1=img.read(1)
img_band2=img.read(2)
img_band3=img.read(3)

fig = plt.figure(figsize=(10,10))
ax1 = fig.add_subplot(2,2,1)
ax1.imshow(img_band1, cmap='pink')
ax2 = fig.add_subplot(2,2,2)
ax2.imshow(img_band2, cmap='pink')
ax3 = fig.add_subplot(2,2,3)
ax3.imshow(img_band3, cmap='pink')

#To find out the coordinate reference system
print("Coordinate reference system: ", img.crs)
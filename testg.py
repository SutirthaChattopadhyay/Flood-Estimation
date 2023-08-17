import rasterio
from rasterio.plot import show
import matplotlib.pyplot as plt

img_data = rasterio.open('E:\Only-CO-Lang\Python Code\CODE-py\Flood Ai\mine\srm\example_highlighted.tif')
fig, ax = plt.subplots(figsize=(10,10))    
show(img_data)
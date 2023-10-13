from scipy.ndimage import gaussian_filter as gf
import matplotlib.pyplot as plt

load_image=plt.imread("imgs/image.jpeg")
blured_image=gf(load_image,2)

prefix='Blured_'

plt.subplot(121)
plt.imshow(load_image)
plt.title("Original Image")

plt.subplot(122)
plt.imshow(blured_image)
plt.title("Blured_image")

blured_image_name= prefix + "1.png"
plt.imsave(blured_image_name, blured_image)

plt.show()

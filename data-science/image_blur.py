from scipy.ndimage import gaussian_filter as gf
import matplotlib.pyplot as plt

load_image=plt.imread("imgs/image1.png")
blurred_image=gf(load_image, 2)

prefix="blurred_"

plt.subplot(121)
plt.imshow(load_image)
plt.title("Original Image")

plt.subplot(122)
plt.imshow(blurred_image)
plt.title("Blurred Image")

blurred_image_name= prefix + "1.png"
plt.imsave(blurred_image_name, blurred_image)

plt.show()
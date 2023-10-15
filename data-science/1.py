import scipy.ndimage as ndimage
import matplotlib.pyplot as plt

image = plt.imread('image1.png')
blurred_image = ndimage.gaussian_filter(image, sigma=2)
plt.subplot(121)
plt.imshow(image)
plt.title('Original Image')

plt.subplot(122)
plt.imshow(blurred_image)
plt.title('Blurred Image')

prefix = 'blurred_'
blurred_image_name = prefix + 'example_image.jpg'
plt.imsave(blurred_image_name, blurred_image)

plt.show()

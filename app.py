from PIL import Image
import numpy as np

# raw data of image
# this np object is not an actuall object
im_raw = np.array(Image.open('chill.jpg'))

print(f'------------------------------ image details ------------------------------')
print(f'array dimensions: {im_raw.ndim}')
print(f'image pixel height: {len(im_raw)}')
print(f'image pixel width: {len(im_raw[0])}')
print(f'---------------------------------------------------------------------------')

# print(im_raw[0,0])
count = 0
for row in im_raw:
    for pixel in row:
        rgb_value = int(pixel[0]) + int(pixel[1]) + int(pixel[2])
        if rgb_value < 300:
            pixel[0] = 1
            pixel[1] = 1
            pixel[2] = 1
        else:
            pixel[0] = 255
            pixel[1] = 255
            pixel[2] = 255


from PIL import Image
import numpy as np

##################################### CONFIG
# image file
image_file = 'k-on.jpg'
# dimensions
keep_aspect_ratio = True
dimensions = (130,150) # (width, height)
# testing
display_image = False 

##################################### SOME FUNCTIONS
# calculates avg value of rgb of a single pixel.
def compute_avg_rgb(pixel):
    return (int(pixel[0]) + int(pixel[1]) + int(pixel[2]))/3

# sets the colour of a specific pixel.
def set_pixel_colour(pixel,rgb):
    for i in range(3):
        pixel[i] = rgb[i]

##################################### INIT RESULT
ascii_image = []

# opening the image
image = Image.open(image_file)
# resizing the image
if keep_aspect_ratio:
    image.thumbnail(dimensions)
else:
    image.resize(dimensions)

# convert image into raw (numpy array) format
image_raw = np.array(image)

row_index = 0
for row in image_raw:
    # enter into the row.
    ascii_image.append([])
    for pixel in row:
        # enter into the pixel.
        avg_rgb = compute_avg_rgb(pixel)
        if avg_rgb < 30:
            ascii_image[row_index].append('█')
        elif avg_rgb < 135:
            ascii_image[row_index].append('▓')
        elif avg_rgb < 170:
            ascii_image[row_index].append('▒')
        elif avg_rgb < 200:
            ascii_image[row_index].append('░')
        elif avg_rgb < 240:
            ascii_image[row_index].append('.')
        else: 
            ascii_image[row_index].append(' ')
    
    row_index += 1

for row in ascii_image:
    for ascii_key in row:
        print(ascii_key,end='')
    print('')

# just for testing
if display_image:
    # convert image into displayable format
    im = Image.fromarray(image_raw)
    # display image
    im.show()

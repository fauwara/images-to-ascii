from PIL import Image
import numpy as np

# raw data of image
# this np object is not an actuall object
im_raw = np.array(Image.open('lmao.png'))

print(f'------------------------------ image details ------------------------------')
print(f'array dimensions: {im_raw.ndim}')
print(f'image pixel height: {len(im_raw)}')
print(f'image pixel width: {len(im_raw[0])}')
print(f'---------------------------------------------------------------------------')

# print(im_raw)
im_height = len(im_raw)
im_width = len(im_raw[0])

px = 50
count = 0

pixel_comp_h = int(im_height/px)*2

pixel_comp_w = int(im_width/px)

start_index_h = 0
end_index_h = int(im_height/px)

start_index_w = 0
end_index_w = int(im_width/px)

row_list = []
colomn_list = []

for i in range(0,im_width,pixel_comp_w):
    row_list.append([i,i+pixel_comp_w])

b = []

for i in range(0,im_height,pixel_comp_h):
    c = [i,i+pixel_comp_h]
    b.append([c,row_list])

# b = [[[0,end_index_h],row_list],[[end_index_h,end_index_h*2],row_list]]

res = []

for i in b:
    for j in range(len(row_list)):
        # print(j)
        avg_r = 0
        avg_g = 0
        avg_b = 0
        res.append([])

        for row_index in range(i[0][0],i[0][1]):
            avg_row_r = 0
            avg_row_g = 0
            avg_row_b = 0

            for pixel_index in range(i[1][j][0],i[1][j][1]):
                avg_row_r += im_raw[row_index,pixel_index,0]
                avg_row_g += im_raw[row_index,pixel_index,1]
                avg_row_b += im_raw[row_index,pixel_index,2]

            avg_r += int(avg_row_r/end_index_w)
            avg_g += int(avg_row_g/end_index_w)
            avg_b += int(avg_row_b/end_index_w)

        rgb_value = int(int((avg_r/pixel_comp_h) + int(avg_g/pixel_comp_h) + int(avg_b/pixel_comp_h))/3)
        # print(rgb_value)

        if rgb_value < 30:
            res[j].append('█')
        elif rgb_value < 135:
            res[j].append('▓')
        elif rgb_value < 170:
            res[j].append('▒')
        elif rgb_value < 200:
            res[j].append('░') 
        elif rgb_value < 240:
            res[j].append('.')
        else: 
            res[j].append(' ')                  
            #im_raw[row_index,pixel_index,0] = 0
        #im_raw[row_index,pixel_index,1] = 0
        #im_raw[row_index,pixel_index,2] = 0
    # print(im_raw[row_index])
    
for i in range(px):
    for j in range(px):
        print(res[j][i],end = '')
    print('')

import numpy as np
from numpy import array
import matplotlib.image as mpimg
import math


def psnr(img1, img2):
    mse = np.mean( (img1 - img2) ** 2 )
    if mse == 0:
        return 100
    PIXEL_MAX = 255.0
    return 20 * math.log10(PIXEL_MAX / math.sqrt(mse))


print('')
encode_this_raw = input('Enter the data to be encoded : ')
print('Data to be encoded is : ', encode_this_raw)

length_of_raw_data = len(encode_this_raw)
string_of_binary_data_to_be_incoded = ''
b = ''

for x in range(0, length_of_raw_data):
    encode_this_raw_data_element = encode_this_raw[x]
    ascii_data = ord(encode_this_raw_data_element)
    binary_data = bin(ascii_data)
    length_of_binary_data =(len(binary_data))
    only_this = binary_data[2:(length_of_binary_data + 1)]
    string_of_binary_data_to_be_incoded = (string_of_binary_data_to_be_incoded + only_this)    

pixel_list = []
print('')
image_is = mpimg.imread("xyz.jpg")
r1, c1, p1 = image_is.shape
print('Number of rows in 1 image   : %d \nNumber of column in 1 image : %d \nNumber of pages in 1 image  : %d' % (r1, c1, p1))

for i in range(0,r1):
    for j in range(0,c1):
        for k in range(0,p1):
            pixel_list.append(image_is[i, j, k])

length_of_string_of_binary_data_to_be_incoded = len(string_of_binary_data_to_be_incoded)
new_array = np.array(pixel_list)
length_new_array = len(new_array)

if (length_of_string_of_binary_data_to_be_incoded <= length_new_array):
    for x in range(0, length_of_string_of_binary_data_to_be_incoded):
        encode_this_to_lsb = string_of_binary_data_to_be_incoded[x]
        a = new_array[x]
        a = int(a)
        binary_value = bin(a)
        length_binary_value = len(binary_value)
        only_this = binary_value[2:(length_binary_value + 1)]
        length_only_this = len(only_this)
        for el in range(0,(length_only_this - 1)):
            b = b + only_this[el]
        b = b + encode_this_to_lsb
        c = int(b, 2)
        new_array[x] = c
        b = ''
    
print('')
gen_image_is = new_array.reshape(1365, 2048, 3)
mpimg.imsave('lsbencoded.jpg', gen_image_is)
r2, c2, p2 = gen_image_is.shape
print('Number of rows in 2 image   : %d \nNumber of column in 2 image : %d \nNumber of pages in 2 image  : %d' % (r2, c2, p2))
print('')
print('Element from image 1  : ', image_is[0, 1, 1])
print('Element from image 2  : ',gen_image_is[0,1,1])
print('')

original = image_is
contrast = image_is
d=psnr(original,contrast)
print('PSNR for orignal is   : ', d)

original = gen_image_is
contrast = gen_image_is
d=psnr(original,contrast)
print('PSNR for generated is : ', d)

original = image_is
contrast = gen_image_is
d=psnr(original,contrast)
print('PSNR is               : ', d)





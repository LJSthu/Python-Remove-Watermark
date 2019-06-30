from skimage import io
from pdf2image import convert_from_path
import numpy as np
# imgs = io.imread('./test.png')
# io.imsave('./hh.png',imgs)
# imgs = np.array(imgs)
# print(imgs.shape)
# r = []
# g = []
# b = []
# alpha = []

def judge(x,y):
    temp = -(600.0/1575.0) * x
    if y > 1350 + temp and y < 1500 + temp:
        return True
    else:
        return False

# for  i in range(imgs.shape[0]):
#     for j in range(imgs.shape[1]):
#         if not judge(j,i):
#             continue
#         if imgs[i][j][1] > 100 and imgs[i][j][1] < 250 and imgs[i][j][2] > 100 and imgs[i][j][2] < 250:
#             imgs[i][j][0] =  imgs[i][j][1] = imgs[i][j][2] = 255
#         if imgs[i][j][1] < 10 and imgs[i][j][2] < 100:
#             imgs[i][j][0] =  imgs[i][j][1] = imgs[i][j][2] = 0 

# io.imsave('./hh.png',imgs)
# print(r)
# print(g)
# print(b)
# print(alpha)

def select_pixel(r,g,b):
    if (r == 208 and g == 208 and b == 208 ) or (r == 196 and g == 196 and b == 196) \
        or (r == 206 and g == 206 and b == 206 ):
        return True
    else:
        return False
def select_pixel2(r,g,b):
    if r > 175 and r < 250 and g > 175 and g < 250 and b > 175 and b < 250:
        return True
    else:
        return False
def handle(imgs):
    for  i in range(imgs.shape[0]):
        for j in range(imgs.shape[1]):
            # if not judge(j,i):
            #     continue
            # if imgs[i][j][1] > 100 and imgs[i][j][1] < 250 and imgs[i][j][2] > 100 and imgs[i][j][2] < 250:
            if select_pixel2(imgs[i][j][0],imgs[i][j][1],imgs[i][j][2]):
                imgs[i][j][0] =  imgs[i][j][1] = imgs[i][j][2] = 255
            # if not select_pixel(imgs[i][j][0],imgs[i][j][1],imgs[i][j][2]):
            #     imgs[i][j][0] =  imgs[i][j][1] = imgs[i][j][2] = 0 
    return imgs

images = convert_from_path('./jiangyi3.pdf')
# images = np.array(images)
index = 0
for img in images:
    index += 1
    img = np.array(img)
    print(img.shape)
    img = handle(img)
    io.imsave('./jiangyi3/img'+str(index)+'.jpg', img)
    # break
    print(index)
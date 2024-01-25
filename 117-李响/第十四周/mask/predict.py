import os
os.environ['HDF5_DISABLE_VERSION_CHECK']='2'
from keras.layers import Input
from mask_rcnn import MASK_RCNN 
from PIL import Image

mask_rcnn = MASK_RCNN()

while True:
    img = input('img/street.jpg')
    try:
        image = Image.open('img/0.jpg')
    except:
        print('Open Error! Try again!')
        continue
    else:
        mask_rcnn.detect_image(image)
mask_rcnn.close_session()
    

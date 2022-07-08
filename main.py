import sys
import numpy as np
import argparse
from PIL import Image, ImageEnhance

def pixellize(**kwargs):

    # load image
    #img_name = "test.jpg"
    #img_name = "./examples/original/test.jpg"
    if "img_path" not in list(kwargs.keys()):
        raise KeyError("Image path is not given.")
    elif "save_path" not in list(kwargs.keys()):
        raise KeyError("Save path is not given.")
    else:
        img_name = kwargs["img_path"]
        save = kwargs["save_path"]

    img = Image.open(img_name)
    img_size = img.size

    # boost saturation of image 
    sat_booster = ImageEnhance.Color(img)
    img = sat_booster.enhance(float(kwargs.get("saturation", 1.25)))

    # increase contrast of image
    contr_booster = ImageEnhance.Contrast(img)
    img = contr_booster.enhance(float(kwargs.get("contrast", 1.2)))

    # reduce the number of colors used in picture
    img = img.convert('P', palette=Image.ADAPTIVE, colors=int(kwargs.get("n_colors", 10)))

    # reduce image size
    superpixel_size = int(kwargs.get("superpixel_size", 10))
    print(superpixel_size)


    #### B_edit:
    
    ## resize image with given image size 
    # 0: original
    # 1: superpixel size defines output image size
    # 2: user_defined image_size (x_dim, y_dim)
        
    define_new_size = int(kwargs.get("new_size"),0)
    new_dim_x = int(kwargs.get("new_x_dim",32))
    new_dim_y = int(kwargs.get("new_y_dim",32))
    # print("___Pixelate___ : define_new_size param", define_new_size)
    # print("___Pixelate___ : new_x_dim param", new_dim_x)
    # print("___Pixelate___ : new_y_dim param", new_dim_y)

    if define_new_size == 0:
        print("___Pixelate___ : original size", img_size)
        reduced_size = (img_size[0] // superpixel_size, img_size[1] // superpixel_size)
        img = img.resize(reduced_size, Image.BICUBIC)
        # resize to original shape to give pixelated look
        img = img.resize(img_size, Image.BICUBIC)
        img.save(save)
    elif define_new_size == 1:
        reduced_size = (img_size[0] // superpixel_size, img_size[1] // superpixel_size)
        print("___Pixelate___ : superpixel param defines size", reduced_size)    
        img = img.resize(reduced_size, Image.BICUBIC)
        img.save(save)
        
    elif define_new_size == 2 and new_dim_x is not None:
        ## B, non-rectangular shapes work as well
        print("___Pixelate___ : user defined img size", new_dim_x,new_dim_y )
        #convert to small image
        small_img=img.resize((new_dim_x,new_dim_y),Image.BILINEAR)
        small_img.save(save)
        
    #### B_end edit    
    

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('img_path')
    parser.add_argument('save_path')
    # parser.add_argument('--name', type=str, required=True)
    parser.add_argument('--num_color', default=2 , required=True, nargs="?")
    parser.add_argument('--superpixel_size', default=2, required=True, nargs="?")
    parser.add_argument('--saturation', default=1.5 , required=True, nargs="?")
    parser.add_argument('--contrast', default=1.7 , required=True, nargs="?")
    parser.add_argument('--new_size', default=0 , required=True, nargs="?")
    parser.add_argument('--new_x_dim', default=32 , required=False, nargs="?")
    parser.add_argument('--new_y_dim', default=32 , required=False, nargs="?")


    kwargs = vars(parser.parse_args())

    print(type(kwargs))

    pixellize(**kwargs)

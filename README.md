# pixelate

pixelate turns your pictures into pixel art ! Well, sometimes.

It is a simple script based on PIL.

<img src="/examples/akira.jpg" alt="" width="400"/> <img src="/examples/akira_pix.png" alt="" width="400"/>  

<img src="/examples/kid.jpg" alt="" width="400"/> <img src="/examples/kid_pix.png" alt="" width="400"/>  

Algorithms will be added in the future. More precisely, I'd like to try to learn a mapping between input and pixelated space with a UNet-like encoder/decoder ConvNet.

## Requirements

It requires recent versions of both numpy and PIL.

`pip install numpy`

`pip install Pillow`

It was tested using Pillow 4.0.0 and numpy 1.12.1.

## Use Case

`python3 main.py examples/jedsy_logo.png examples/test_1.png --num_color 10 --superpixel_size 10 --saturation 1.25 --contrast 1.2`

`num_color` is the amount of colors wanted for the output. Small numbers typically give better results.

`superpixel_size` is the superpixel size. Rule of thumb : the larger the image, the larger the superpixels.

`saturation` is the saturation factor. Saturation helps create similar color zones.

`contrast` is the contrast factor. It is often useful to increase contrast to get better results.

`new_size` is the new size for the output image, three options available currently: 
> 0. original
> 1. superpixel size defines output image size
> 2. user_defined image_size (x_dim, y_dim)

`new_x_dim` is the new pixel size in x dimension.

`new_y_dim` is the new pixel size in x dimension.

If the second argument refers to a folder, by default the name used for saving the processed file will be the same as the original file. An artifact is added if name refers to an existing file. ( B_edit: didn't tested above)

[original work](https://github.com/ferretj/pixelate)

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

`python3 main.py examples/aaa.jpg examples/aaa_12.png`

` B edit parameter allocation is buggy `

`python main.py imgs/test.png pixelated/test.png -n 10 -p 10 -s 1.25 -c 1.2`

`n` is the amount of colors wanted for the output. Small numbers typically give better results.

`p` is the superpixel size. Rule of thumb : the larger the image, the larger the superpixels.

`s` is the saturation factor. Saturation helps create similar color zones.

`c` is the contrast factor. It is often useful to increase contrast to get better results.

If the second argument refers to a folder, by default the name used for saving the processed file will be the same as the original file. An artifact is added if name refers to an existing file.


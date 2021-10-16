from tkinter import *
import glob
from os.path import isfile, join
import os
from os import listdir
from tkinter import messagebox
from tkinter.filedialog import askopenfile
from PIL import Image
import os



def select_file():
    file_path = askopenfile(title='Open a image',
                            initialdir='C:\\Users\\Alks\\Desktop\\Project\\pythonProject\\PhotoFromPhoto\\BasicPhoto')
    output_pixfile_path = 'C:\\Users\\Alks\\Desktop\\Project\\pythonProject\\PhotoFromPhoto\\OutPutPhoto\\'
    p = str(file_path.name)
    output_pixfile_path = (output_pixfile_path+os.path.basename(p))
    pixelate(file_path.name, output_pixfile_path, pixel_size)
    global output_pixfile_path_return
    output_pixfile_path_return = output_pixfile_path


def pixelate(input_file_path, output_pixfile_path, pixel_size):
    image = Image.open(input_file_path)
    image = image.resize(
        (image.size[0] // pixel_size, image.size[1] // pixel_size),
        Image.NEAREST
    )
    image = image.resize(
        (image.size[0] * pixel_size, image.size[1] * pixel_size),
        Image.NEAREST
    )
    image.save(output_pixfile_path)


# def dominate_pixels():
#     path_to_f = "C:\\Users\\Alks\\Desktop\\Project\\pythonProject\\PhotoFromPhoto\\OutPutPhoto"
#     f = listdir(path_to_f)
#     im = Image.open("C:\\Users\\Alks\\Desktop\\Project\\pythonProject\\PhotoFromPhoto\\OutPutPhoto\\" + f[0])
#     img_data = list(im.getdata())
#     for big_pixel in img_data:
#         filter(if )
#
#     print(img_data[0])



def crop_img():
    path_to_f = "C:\\Users\\Alks\\Desktop\\Project\\pythonProject\\PhotoFromPhoto\\Pictures\\"
    for f in listdir(path_to_f):
        if f.endswith('.jpg'):
            im = Image.open("C:\\Users\\Alks\\Desktop\\Project\\pythonProject\\PhotoFromPhoto\\Pictures\\"+f)
            image = im.resize(
                (pixel_size, pixel_size),
                Image.NEAREST)
            # width, height = im.size
            # if width > 1440:
            #     crop_width = (width - 1400)/2
            # else:
            #     crop_width = width
            # if height > 1440:
            #     crop_height = (height - 1400)/2
            # else:
            #     crop_height = height
    # im = im.crop((crop_width, crop_height, crop_width, crop_height))
    #         im = im.crop((240, 240, 1680, 1680))
            image.save('C:\\Users\\Alks\\Desktop\\Project\\pythonProject\\PhotoFromPhoto\\Pictures\\CUT\\'+f)


def read_img(input_pixfile_path):
    im = Image.open(input_pixfile_path, 'r')
    width, height = im.size
    img_data = list(im.getdata())
    print(img_data[1:3])
    # x_pos = 0
    # y_pos = 1
    #
    # pixel_value = []
    # x = []
    # y = []
    # for pix in img_data:
    #     if x_pos == width:
    #         x_pos = 1
    #         y_pos += 1
    #     else:
    #         x_pos += 1
    #     pixel_value.append(pix[2])
    #     x.append(x_pos)
    #     y.append(y_pos)
    # print()


def start_program():
    read_img(output_pixfile_path_return)


def dominant_color():
    path_to_f = "C:\\Users\\Alks\\Desktop\\Project\\pythonProject\\PhotoFromPhoto\\Pictures\\CUT\\"
    for f in listdir(path_to_f):
        if f.endswith('.jpg'):
            im = Image.open("C:\\Users\\Alks\\Desktop\\Project\\pythonProject\\PhotoFromPhoto\\Pictures\\CUT\\" + f, 'r')

            image = im.resize((1, 1),)
            imdata = image.getdata()
            print(list(imdata[0]))

            image.save("C:\\Users\\Alks\\Desktop\\Project\\pythonProject\\PhotoFromPhoto\\Pictures\\CUT\\" + '1' + f)




window = Tk()
window.title('PhotoFromPhoto')
window.geometry('300x250')

# dominate_pixels()
list1 = [2,3,4,3,10,3,5,6,3]
listnew = []
# print(list1.count(3))
for n in list1:
    print(n)
    print(list1.count(n))
    elem = filter(lambda n: list1.count(n)//2 == 0, list1)
    print(list(elem))
#     listnew = listnew.append(list(elem))
# print('The count of element: 3 is ', listnew)
# dominant_color()

# pixel_size = 35
# crop_img()
#
# clean_img = Image.new(mode='RGB', size=(1440, 1440))
# # clean_img.show()
#
# main_menu = Menu()
# main_menu.add_cascade(label='Select File',
#                       command=select_file)
# output_pixfile_path_return = ''
# main_menu.add_cascade(label='Start',
#                       command=start_program)
#
# window.config(menu=main_menu)

window.mainloop()

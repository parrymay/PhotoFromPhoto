import tkinter
from shutil import copyfile
import tkinter.filedialog
from distutils.dir_util import copy_tree
from tkinter import *
import glob
from os.path import isfile, join
import os
from os import listdir
from os import path
from tkinter import messagebox
from tkinter.filedialog import askopenfile
from tkinter.filedialog import askdirectory
from PIL import Image
import os


def select_f():
    path_f = askopenfile(title='Open your image',
                         initialdir=os.getcwd(),
                         filetypes=[('JPG', '*.jpg')])
    path_f = path_f.name
    path_pixelate = pixelate(path_f)
    return path_f.name, path_pixelate


def pixelate(path_f):
    pixel_sizes = int(pix_size.get())
    index = path_f.index('.')
    path_temp = path_f[:index]
    path_temp = path_temp + 'temp' + '.jpg'
    copyfile(path_f, path_temp)
    low_q_image = Image.open(path_temp)
    low_q_image = low_q_image.resize((low_q_image.size[0] // pixel_sizes,
                                      low_q_image.size[1] // pixel_sizes),
                                      Image.NEAREST)
    low_q_image = low_q_image.resize((low_q_image.size[0] * pixel_sizes,
                                      low_q_image.size[1] * pixel_sizes),
                                      Image.NEAREST)
    low_q_image.save(path_temp)
    path_pixelate = path_temp
    return path_pixelate


def dominate_color(path):
    path_temp = path + 'temp2'
    copy_tree(path, path_temp)
    for f in listdir(path_temp):
        if f.endswith('.jpg'):
            im = Image.open(path_temp + '/' + f)
            im = im.resize((1, 1), Image.BILINEAR)  # Play with it
            img_data = list(im.getdata())
            print(img_data)
            im.save(path_temp + '/' + f)


def crop_photos(path):
    pixel_sizes = int(pix_size.get())
    path_temp = path + 'temp1'
    copy_tree(path, path_temp)
    for f in listdir(path_temp):
        im = Image.open(path_temp + '/' + f)
        im = im.resize((pixel_sizes, pixel_sizes), Image.NEAREST)
        im.save(path_temp + '/' + f)


def paste(path):
    im = Image.open()
    width, height = im.size
    print(width)
    big_pixel_Y = height//pix_size
    big_pixel_X = width//pix_size
    im = Image.open(path)
    data = []
    for pixel_Y in range(1, big_pixel_Y):
        pixel_Y = pixel_Y*big_pixel_Y
        for pixel_X in range(1, big_pixel_X):
            pix_data = list(im.getdata())
            data.append([pixel_X], [pixel_Y], pix_data)


# def read_img(input_pixfile_path):
#     im = Image.open(input_pixfile_path, 'r')
#     width, height = im.size
#     img_data = list(im.getdata())
#     print(img_data[1:3])
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


def select_dir():
    path_dir = askdirectory(title='Open dir with many photos', initialdir=os.getcwd())
    crop_photos(path_dir)
    dominate_color(path_dir)
    return path_dir


def delete_temp():
    return


def start_program():

    return


def save_f():
    return


window = Tk()
window.title('PhotoFromPhotos')
window.geometry('1440x1440')
window.resizable(width=False, height=False)

main_menu = Menu()

main_menu.add_command(label='1.Select InitPhoto -> |',
                      command=select_f)

main_menu.add_command(label='2.Select Directory -> |',
                      command=select_dir)

main_menu.add_command(label='3.Start -> |',
                      command=start_program)

main_menu.add_command(label='4.Save',
                      command=save_f)

tkinter.Label(text="Размер пикселя").grid(row=0, column=1)
pix_size = tkinter.StringVar(value=40)
tkinter.Entry(textvariable=pix_size).grid(row=0, column=2)


window.config(menu=main_menu)
window.mainloop()


# dominate_pixels()
# list1 = [2,3,4,3,10,3,5,6,3]
# listnew = []
# print(list1.count(3))
# for n in list1:
#     print(n)
#     print(list1.count(n))
#     elem = filter(lambda n: list1.count(n)//2 == 0, list1)
#     print(list(elem))
#     listnew = listnew.append(list(elem))
# print('The count of element: 3 is ', listnew)
# dominant_color()

# pixel_size = 35
# crop_img()
#
# clean_img = Image.new(mode='RGB', size=(1440, 1440))
# # clean_img.show()


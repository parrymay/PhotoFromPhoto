from shutil import copyfile
import tkinter.filedialog
from tkinter import *
from tkinter import messagebox
from os import listdir
from tkinter.filedialog import askopenfile
from tkinter.filedialog import askdirectory
from PIL import Image
import os
import math
import shutil


def select_f():
    path_f = askopenfile(title='Open your image',
                         initialdir=os.getcwd(),
                         filetypes=[('JPG', '*.jpg')])
    messagebox.showinfo('Information', 'Wait about 2 minute')
    path_f = path_f.name
    path_pixelate = pixelate(path_f)
    compare_color(path_pixelate, path_dir)


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


def crop_photos(path_dir):
    pixel_sizes = int(pix_size.get())
    path_temp = path_dir + 'temp1'
    os.mkdir(path_temp)
    for f in listdir(path_dir):
        im = Image.open(path_dir + '/' + f)
        im = im.resize((pixel_sizes, pixel_sizes), Image.NEAREST)
        im.save(path_temp + '/' + f)


def compare_color(path_init_photo, path_dir):
    # for i in range(0, 400):
        # url = 'https://picsum.photos/100'
        # img = urllib.request.urlopen(url).read()
        # out = open('img' + str(i) + '.jpg', "wb")
        # out.write(img)
        # out.close()
    pixel_sizes = int(pix_size.get())
    im = Image.open(path_init_photo)
    # im = im.convert('RGBA')
    width, height = im.size
    big_pixel_Y = height//pixel_sizes
    big_pixel_X = width//pixel_sizes
    image_pix_data = im.load()
    for pixY in range(0, big_pixel_Y):
        pixY = pixY*pixel_sizes
        for pixX in range(0, big_pixel_X):
            pixX = pixX*pixel_sizes
            min_diff = 300
            for f in listdir(path_dir):
                if f.endswith('.jpg'):
                    photo_path = path_dir + 'temp1' + '/' + f
                    photo_o = Image.open(photo_path)
                    # photo_o = photo_o.convert('RGBA')
                    photo = photo_o.resize((1, 1), Image.BILINEAR)
                    photo_pix_data = photo.load()
                    difference_color = math.sqrt((image_pix_data[pixX, pixY][0] - photo_pix_data[0, 0][0])**2 +
                                                 (image_pix_data[pixX, pixY][1] - photo_pix_data[0, 0][1])**2 +
                                                 (image_pix_data[pixX, pixY][2] - photo_pix_data[0, 0][2])**2)
                    if difference_color < min_diff:
                        min_diff = difference_color
                        path_to_min = photo_o
            im.paste(path_to_min, (pixX, pixY))
    im.show()
    # im.save("new.jpg")
    for folder in listdir(os.getcwd()):
        a = folder.find('temp')
        if a != -1:
            shutil.rmtree(folder)


def select_dir():
    global path_dir
    path_dir = askdirectory(title='Open dir with many photos', initialdir=os.getcwd())
    crop_photos(path_dir)
    return path_dir


def save_f(im):
    save_path = askopenfile(title='Open dir for save result')
    im.save(save_path + '/' + 'result.jpg')
    return


window = Tk()
window.title('PhotoFromPhotos')
window.geometry('1440x1440')
window.resizable(width=False, height=False)

main_menu = Menu()

main_menu.add_command(label='1.Select Photos Directory -> |',
                      command=select_dir)

main_menu.add_command(label='2.Select InitPhoto -> |',
                      command=select_f)

# main_menu.add_command(label='3.Save',
                      # command=save_f)

tkinter.Label(text="Размер пикселя").grid(row=0, column=1)
pix_size = tkinter.StringVar(value=40)
tkinter.Entry(textvariable=pix_size).grid(row=0, column=2)


window.config(menu=main_menu)
window.mainloop()


# clean_img = Image.new(mode='RGB', size=(1440, 1440))
# # clean_img.show()

# try except

# def delete_temp():
#     return

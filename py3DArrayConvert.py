import scipy.io as sio
import imageio
import numpy as np
import cv2
import os

"""
Author: Ki Min Lee

dependencies: 
    scipy
    imageio
    numpy
    cv2
    python3
"""

# configuration variables
x = 0  # x-axis value
y = 0  # y-axis value
z = 0  # z-axis value
IMG_TYPE = '.png'  # export image file type, default .jpg

# default uint8.
# change min, max values for different scaling
SCALE_MAX_VAL = 255
SCALE_MIN_VAL = 0


load_arr = '<file_name>.mat'
save_arr = '<file_name>.mat'

array_name = '<dictionary_key>'
result_array_name = array_name

directory = 'export'
parents_dir = os.path.dirname(__file__)

# intialize empty 3D array for result
arr = np.zeros((x, y, z), dtype='uint8')


def load():
    """ 
    Loads the training set in data_set
    returns tuple of specific array in training set and loaded data set
    """
    print("Loading dataset " + load_arr + "...")
    try:
        data_set = sio.loadmat(load_arr)
        data_arr = data_set[array_name]
        arr = np.copy(data_arr)
        print("Loading complete")
        return (data_arr, data_set)
    except:
        print("Unsuccessful load")


def convert_img(img):
    """
    converts image array to uint8, scaling it within 0-255 range
    returns converted image
    """
    return cv2.normalize(src=img, dst=None, alpha=SCALE_MIN_VAL, beta=SCALE_MAX_VAL, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8U)


def convertData(data_arr):
    """ 
    iterates through each images in the 3d array and normalizes the image 
        passes each image to convert()
    """
    try:
        print("Converting specified data " + array_name + "...")
        for img in range(0, z):
            arr[:, :, img] = convert_img(data_arr[:, :, img])
        print("Conversion complete")
    except Exception as e:
        print("Unsuccessful conversion. Error: " + repr(e))


def save(data_set):
    """
    saves the new data set into separate .mat file
    """
    try:
        print("Saving dataset into " + result_array_name + "...")
        data_set[result_array_name] = arr
        sio.savemat(save_arr, data_set)
        print("Saving complete")
    except Exception as e:
        print("Unsuccessful save. Error: " + repr(e))


def export_img():
    """
    creates new directory for image storage, if it doesn't exist
    exports each layer of image with file name <layer_num>.jpg
    """
    path = os.path.join(parents_dir, directory)
    if not os.path.exists(path):
        print("Creating directory: " + path + "...")
        os.mkdir(path)
    try:
        print("Exporting images to " + path + "...")
        for img_count in range(0, z):
            imageio.imwrite(path + str(img_count) + IMG_TYPE,
                            arr[:, :, img_count])
        print("Export complete")
    except Exception as e:
        print("Unsuccessful export. Error: " + repr(e))


def convert():
    (data_arr, data_set) = load()
    convertData(data_arr)
    save(data_set)
    export_img()

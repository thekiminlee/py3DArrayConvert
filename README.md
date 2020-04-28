# 3D Array Image Converter

<h3>Python program that allows conversion of <em>dtype=double</em> to <em>dtype=uint8</em> in 3D array of .mat files. <br> 
The conversion will convert from input array's scale of <em>(double_min, double_max)</em> to uint8 <em>(0, 255)</em> <br> 
Result array is stored in a separate .mat file, added to the existing dict with new key <<em>result_array_name</em>> <br> 
Result array is exported to <<em>IMAGE_TYPE</em>> (default .png) file in a separate directory</h3>

<br>

## Dependencies

- scipy
- imageio
- numpy
- cv2
- python3

<br>

## Converting 3D array

Import py3DArrayConvert.py and define **user-defined values** listed below

### Pre-defined values

_`IMG_TYPE`_ : image format for export. Default = .png <br>
_`SCALE_MIN_VAL`_ : min value for uint8 scale. Default = 0 <br>
_`SCALE_MAX_VAL`_ : max value for uint8 scale. Default = 255 <br>

### User-defined values

_`x`_ : x-axis value of 3D array. Default = 0<br>
_`y`_ : y-axis value of 3D array. Default = 0 <br>
_`z`_ : z-axis value of 3D array. Default = 0 <br>
_`load_arr`_ : path to loading array .mat file (e.g. ~/path/filename.mat) <br>
_`save_arr`_ : path to saving array .mat file (e.g. ~/path/save.mat) <br>
_`array_name`_ : name of the dictionary key in the array <br>
_`result_array_name`_ : name of the resulting dictionary key, for export/save. Default = _`array_name`_ (Will overwrite existing dictionary) <br>
_`directory`_ : name of the directory for image export. Will create new directory if it does not exist. Default = _export/_ <br>
_`parent_dir`_ : path to the parent directory of above directory value. Default = _current working directory_<br>

### Conversion

- define above values and run `convert()`

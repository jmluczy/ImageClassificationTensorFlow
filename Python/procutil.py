"""
Hold various utils for processing / manipulating the leaf image dataset.
"""
import os
import shutil
import cv2
from matplotlib import pyplot as plt
import numpy as np

# BASE_PATH = 'C:\\Users\\jmluc\\Documents\\capstone\\leafdata\\images'
BASE_PATH = '<DIRECTORY HOLDING "lab" AND "field" FOLDERS>'


def copy_files(to_path, from_path=BASE_PATH):
    """Copy all files in the from_path directory to the to_path folder
    
       Args:
           to_path   (str): directory to copy files to
           from_path (str): directory to copy files from (default | BASE_PATH)
    """
    try:
        shutil.copytree(from_path, to_path)
    except OSError as exc:
        if exc.errno == errno.ENOTDIR:
            shutil.copy(from_path, to_path)
        else:
            raise exc
            
def list_image_paths(base_dir=BASE_PATH):
    """ Return list of full paths of all files within the base directory.
        Does this by iterating through each item (folders and files) in current directory
            if file then append to list
            if folder then search recursively on that list.
    """
    def append_items(current_dir, the_list):
        subitems = [current_dir + '\\' + folder for folder in os.listdir(current_dir)]
        
        for item in subitems:
            if '.' in item: # its a file
                the_list.append(item) # append its path
            else: # its a subfolder
                append_items(item, the_list) # call append_items on subfolder
    
    the_list = []
    append_items(base_dir, the_list)
    return the_list

    
def show_image(image, colormap='gray', interpolation='bicubic'):
    """show the image using matplotlib.pyplot functions
       RETURN the image resulting from the cv2.imread() function
       
       Args:
           image : can be a (str | filepath) or a numpy.ndarray (values representing pixels)
       """
    if type(image) is str:
        img = cv2.imread(image)
    elif type(image) is np.ndarray:
        img = image
    else:
        raise ValueError("image must be string (image path) or np.ndarray")
    plt.imshow(img, cmap=colormap, interpolation=interpolation)
    plt.xticks([]), plt.yticks([])
    plt.show()
    return img
    
       
if __name__ == '__main__':
    # list of image paths
    im_list = list_image_paths()
    # list of dimensions (h, w) of all images in im_list
    dims = [cv2.imread(im_path).shape[:2] for im_path in im_list]
    
    min_h = min([d[0] for d in dims])
    min_w = min([d[1] for d in dims])
    print('min height:', min_h)
    print('min width: ', min_w, '\n')
    
    max_h = max([d[0] for d in dims])
    max_w = max([d[1] for d in dims])
    print('max height:', max_h)
    print('max width: ', max_w, '\n')
    
    ave_h = sum([d[0] for d in dims]) / len(dims)
    ave_w = sum([d[1] for d in dims]) / len(dims)
    print('ave height:', ave_h)
    print('ave width: ', ave_w, '\n')
    
    # maximum aspect ratio
    max_ratio = max([ max(d[0]/d[1], d[1]/d[0]) for d in dims])
    print('max ratio: ', max_ratio, '\n')
    
    # index of the file with the maximum ratio
    ind_max_rat = [i for i in range(len(dims)) if dims[i][0]/dims[i][1] == max_ratio or dims[i][1]/dims[i][0] == max_ratio]
    im = im_list[ind_max_rat[0]]
    show_image(im)
    
    


import os, sys, pathlib, filter
from argparse import ArgumentParser

#parser = Argument

class PyDisposable:
    def __init__(self):
        self.processed_images = []
        self.filters = None
    
    def validate_image_path(self, image_path):
        return os.path.exists(image_path)

    def construct_pathlib_for_image(image_path):
        return pathlib.Path(image_path)

    def filter_images(self, filter="disposable", *args):
        for image in args:
            # test path validity
            if validate_image_path(image):
                image_pathlib = construct_pathlib_for_image(image)
                image_path = image_pathlib.absolute()
            else:
                raise FileNotFoundError("The image you're trying to filter doesn't exist!")
            self.processed_images.append(image_path)
        return []

    def save_filtered_images(self):
        # how do we deal with images that are floating in memory? Shouldn't we write them to disk?
        # at that point this becomes a command line tool, not a library for use in other files
        pass
"""
1. import pillow, PIL, dependencies
2. parse arguments
3. import separate file, determine and run filters
4. export based on flags - directory
"""

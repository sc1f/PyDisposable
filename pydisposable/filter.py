import os, sys, pathlib
from PIL import Image, ImageEnhance

class Filter:
    filter_types = ["disposable"]
    
    def filter_single_image(self, image_path, filter="disposable"):
        # assume valid path
        if filter not in filter_types:
            throw ValueError("Filter type does not exist!")
        image = Image(image_path)
        """
        How do you create a filter that looks like a disposable camera?
        1. increase contrast and brightness
        2. increase saturation
        3. create random light leaks
        - use open-source transparent light leaks
        - draw it over the image
        """
        enhance_factor = 1.25
        enhance_brightness = ImageEnhance.Brightness(image).enhance(enhance_factor)
        # enhance_brightness.show()
        enhance_contrast = ImageEnhance.Contrast(enhance_brightness).enhance(enhance_factor)
        # enhance_contrast.show()
        """
        problems: how do we deal with large files? We can't keep it all in memory
        - must write to disk at some point
        """
        # .paste(light_leak, position - a (x,y) tuple, light_leak)

# Adapted from some original code by bennuttall and waveform80
# -------------------------------------------------------------
 
from PIL import Image
from itertools import cycle

# EDIT THESE VALUES ------------------------
filters_dir = "/home/pi/allseeingpi/filters"
filters = ['pumpkin']

# ------------------------------------------


filter = filters[0] # Starting value

def _get_filter_image(filter):
    
    # Open the filter as an Image object
    return Image.open(filters_dir + "/" + filter + ".png")

def _pad(resolution, width=32, height=16):
    # Pads the specified resolution
    # up to the nearest multiple of *width* and *height*; this is
    # needed because filters require padding to the camera's
    # block size (32x16)
    return (
        ((resolution[0] + (width - 1)) // width) * width,
        ((resolution[1] + (height - 1)) // height) * height,
    )

def remove_filters(camera):
    
    # Remove all filters from the camera preview
    for f in camera.filters:
        camera.remove_filter(o) 


def preview_filter(camera=None, filter=None):

    # Remove all filters
    remove_filters(camera)

    # Get an Image object of the chosen filter
    filter_img = _get_filter_image(filter)

    # Pad it to the right resolution
    pad = Image.new('RGB', _pad(camera.resolution))
    pad.paste(filter_img, (0, 0))

    # Add the filter
    camera.add_filter(pad.tobytes(), alpha=128, layer=3)

def output_filter(output=None, filter=None):

    # Take an filter Image
    filter_img = _get_filter_image(filter)

    # ...and a captured photo
    output_img = Image.open(output).convert('RGBA')

    # Combine the two and save the image as output
    new_output = Image.alpha_composite(output_img, filter_img)
    new_output.save(output)

all_filters = cycle(filters)

"""Logic to perform mashup image generation.

Deals with resizing and cropping and blending.
"""
from PIL import Image
from resizeimage import resizeimage


def normalize(pil):
    """Normalize a PIL object so it can be mashed-up with another.

    Make it a standard size: Fill it to fully cover a box, then crop it.
    """
    output_size = (512, 512)
    return resizeimage.resize_cover(pil, output_size)


def mashup_pils(src_pil_one, src_pil_two):
    """Mashup two Source PIL object and return a PIL object of that result."""
    return Image.blend(normalize(src_pil_one), normalize(src_pil_two), 0.5)

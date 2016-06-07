"""imagepipe Logic."""
from io import BytesIO

from PIL import Image

from django.core.files import File

from . import images, models


def create_src_model(src_image_file):
    """Create a new Source model from a Django file of the image and return the
    model.
    """
    src_model = models.Source(image_file=src_image_file)
    src_model.save()
    return src_model


def open_model_as_pil(model):
    """Open a Source or Mashup model as a PIL Image."""
    return Image.open(model.image_file)


def select_srcs_for_mashup():
    """Look in the DB for suitable Sources to mashup.

    Finds the pair of oldest, un-mashed-up Sources.
    """
    return (models.Source.objects
            .filter(mashup=None)
            .order_by('timestamp')[:2])


def save_pil_to_file(pil, name):
    """Save a PIL object to an in-memory Django file under a given name and
    return the file.
    """
    image_file = File(BytesIO())
    pil.save(image_file, format='jpeg')
    image_file.name = name
    return image_file


def create_mashup(src_model_one, src_model_two):
    """Create and return a Mashup from two Sources."""
    src_pil_one = open_model_as_pil(src_model_one)
    src_pil_two = open_model_as_pil(src_model_two)

    mashup_pil = images.mashup_pils(src_pil_one, src_pil_two)
    mashup_image_file = save_pil_to_file(mashup_pil, 'mashup')

    mashup = models.Mashup(image_file=mashup_image_file)
    mashup.save()
    src_model_one.mashup = mashup
    src_model_one.save()
    src_model_two.mashup = mashup
    src_model_two.save()
    return mashup


def attempt_create_mashup():
    """Run Mashup creation code if there are enough Sources availible."""
    unmashed_src_set = select_srcs_for_mashup()
    if len(unmashed_src_set) > 1:
        src_model_one, src_model_two = unmashed_src_set
        create_mashup(src_model_one, src_model_two)


def get_srcs():
    """Get Sources for main page listing."""
    return models.Source.objects.order_by('-timestamp')


def get_mashups():
    """Get Mashups for main page listing."""
    return models.Mashup.objects.order_by('-timestamp')

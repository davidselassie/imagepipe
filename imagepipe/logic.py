"""imagepipe Logic."""
from io import BytesIO
from itertools import chain, zip_longest

from PIL import Image

from django.core.files import File

from resizeimage import resizeimage

from titlecase import titlecase

from . import models


def create_src_model(src_image_file, title):
    """Create a new Source model from a Django file of the image, a title, and
    return the model.
    """
    src_model = models.Source(image_file=src_image_file, title=title)
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
    image_file.name = name + '.jpg'
    return image_file


def create_mashup(src_model_one, src_model_two):
    """Create and return a Mashup from two Sources."""
    src_pil_one = open_model_as_pil(src_model_one)
    src_pil_two = open_model_as_pil(src_model_two)

    mashup_pil = mashup_pils(src_pil_one, src_pil_two)
    mashup_image_file = save_pil_to_file(mashup_pil, 'mashup')
    mashup_title = mashup_titles(src_model_one.title, src_model_two.title)

    mashup = models.Mashup(image_file=mashup_image_file, title=mashup_title)
    mashup.save()
    src_model_one.mashup = mashup
    src_model_one.save()
    src_model_two.mashup = mashup
    src_model_two.save()
    return mashup


def normalize(pil):
    """Normalize a PIL object so it can be mashed-up with another.

    Make it a standard size: Fill it to fully cover a box, then crop it.
    """
    output_size = (512, 512)
    pil_rgb = pil.convert('RGB')
    pil_resized_cropped = resizeimage.resize_cover(
        pil_rgb, output_size, validate=False)
    return pil_resized_cropped


def mashup_pils(src_pil_one, src_pil_two):
    """Mashup two Source PIL object and return a PIL object of that result."""
    return Image.blend(normalize(src_pil_one), normalize(src_pil_two), 0.5)


def mashup_titles(title_one, title_two):
    """Mashup two Source titles.

    Interleave their words and titlecase them.

    >>> mashup_titles('zero one two three', 'four five')
    'Zero Four One Five Two Three'
    """
    title_one_tokens = title_one.split()
    title_two_tokens = title_two.split()
    token_pairs = zip_longest(title_one_tokens, title_two_tokens)
    tokens = chain(*token_pairs)
    interleaved_tokens = (token for token in tokens if token is not None)
    return titlecase(' '.join(interleaved_tokens))


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


def get_mashup(id):
    """Get a specific Mashup by ID."""
    return models.Mashup.objects.get(id=id)

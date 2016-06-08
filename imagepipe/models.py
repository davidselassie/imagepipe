"""imagepipe Models."""
import posixpath
import uuid

from django.db import models


def unique_mashup(_, filename):
    """Return a path in the mashups directory with a unique prefix.

    This ensures no two files will overwrite each other.

    This has to be a plain function for migration serialization.
    """
    random_prefix = str(uuid.uuid4()) + '_'
    return posixpath.join('mashups', random_prefix + filename)


def unique_source(_, filename):
    """Return a path in the mashups directory with a unique prefix.

    This ensures no two files will overwrite each other.

    This has to be a plain function for migration serialization.
    """
    random_prefix = str(uuid.uuid4()) + '_'
    return posixpath.join('sources', random_prefix + filename)


class Mashup(models.Model):
    """Stores a mashed-up combination of two images."""

    image_file = models.ImageField(upload_to=unique_mashup)
    title = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Mashup(id={!r}, title={!r})'.format(
            self.id,
            self.title)


class Source(models.Model):
    """Stores an unmodified user-uploaded image."""

    image_file = models.ImageField(upload_to=unique_source)
    title = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    mashup = models.ForeignKey(
        Mashup,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='sources')

    def __str__(self):
        return 'Source(id={!r}, title={!r})'.format(self.id, self.title)

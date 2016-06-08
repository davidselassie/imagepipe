"""imagepipe Models."""
from django.db import models


class Mashup(models.Model):
    """Stores a mashed-up combination of two images."""

    image_file = models.ImageField(upload_to='mashups')
    title = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Mashup(id={!r}, title={!r})'.format(
            self.id,
            self.title)


class Source(models.Model):
    """Stores an unmodified user-uploaded image."""

    image_file = models.ImageField(upload_to='sources')
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

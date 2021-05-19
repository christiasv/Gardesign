import os
import uuid

from ckeditor.fields import RichTextField
from django.db import models
from model_utils.models import TimeStampedModel


class Blog(TimeStampedModel):
    def image_path(instance, filename):
        filename, file_extension = os.path.splitext(filename)
        ext = filename.split('.')[-1]
        name = "%s.%s" % (uuid.uuid4(), ext)
        return os.path.join(name + file_extension)

    title = models.CharField(max_length=250, verbose_name='titulo')
    user = models.CharField(max_length=250, verbose_name='Usuario')
    descripcion_corta = RichTextField()
    descripcion_larga = RichTextField()
    image = models.ImageField(max_length=1000, upload_to=image_path, null=True, blank=True)

    def __str__(self):
        return '{}'.format(self.title)

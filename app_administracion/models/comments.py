import os
import uuid

from ckeditor.fields import RichTextField
from django.db import models
from django.utils.translation import gettext as _
from model_utils.models import TimeStampedModel


class Comments(TimeStampedModel):
    def image_path(instance, filename):
        filename, file_extension = os.path.splitext(filename)
        ext = filename.split('.')[-1]
        name = "%s.%s" % (uuid.uuid4(), ext)
        return os.path.join(name + file_extension)

    comments = RichTextField(verbose_name='Comentario')
    user = models.CharField(max_length=100, verbose_name='Usuario')
    image = models.ImageField(max_length=1000, upload_to=image_path, null=True, blank=True)

    def __str__(self):
        return f'{self.user}'

    class Meta:
        verbose_name = _('Comentario')
        verbose_name_plural = _('Comentarios')

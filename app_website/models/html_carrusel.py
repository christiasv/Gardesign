import os
import uuid

from ckeditor.fields import RichTextField
from django.db import models
from django.utils.translation import gettext as _
from model_utils.models import TimeStampedModel


class Slider(TimeStampedModel):
    INICIO = 'INICIO'
    TYPE_POSITION = (
        (INICIO, 'INICIO'),
    )

    def image_path(instance, filename):
        filename, file_extension = os.path.splitext(filename)
        ext = filename.split('.')[-1]
        name = "%s.%s" % (uuid.uuid4(), ext)
        return os.path.join(name + file_extension)

    title = models.CharField(max_length=250, blank=True, null=True, verbose_name='Titulo')
    texto = RichTextField(verbose_name='Descripcion')
    photo = models.ImageField(max_length=1000, upload_to=image_path, null=True, blank=True, verbose_name='Foto')
    type = models.CharField(verbose_name='Ubicacion de imagen', max_length=6, choices=TYPE_POSITION, default=INICIO)
    more_info = models.CharField(max_length=750, blank=True, null=True, verbose_name='Hipervinculo (Ver más)')
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name = _('Slider')
        verbose_name_plural = _('Sliders')

    def __str__(self):
        return '{} - {}'.format(self.title, self.type)

import os
import uuid

from ckeditor.fields import RichTextField
from django.db import models
from django.utils.translation import gettext as _
from model_utils.models import TimeStampedModel


class Service(TimeStampedModel):
    def image_path(instance, filename):
        filename, file_extension = os.path.splitext(filename)
        ext = filename.split('.')[-1]
        name = "%s.%s" % (uuid.uuid4(), ext)
        return os.path.join(name + file_extension)

    name = models.CharField(max_length=250, blank=True, null=True, verbose_name='Nombre')
    description = RichTextField(verbose_name='Descripcion')
    description_corta = RichTextField(verbose_name='Descripcion corta')
    cover_image = models.ImageField(max_length=1000, upload_to=image_path, null=True, blank=True,
                                    verbose_name='Imagen de portada')
    more_info = models.CharField(max_length=750, blank=True, null=True, verbose_name='Hipervinculo (Ver más)')

    class Meta:
        verbose_name = _('Servicio')
        verbose_name_plural = _('Servicios')

    def __str__(self):
        return '{}'.format(self.name)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


class GalleryImgService(models.Model):
    def image_path(instance, filename):
        filename, file_extension = os.path.splitext(filename)
        ext = filename.split('.')[-1]
        name = "%s.%s" % (uuid.uuid4(), ext)
        return os.path.join(name + file_extension)

    service = models.ForeignKey(Service, related_name='service', on_delete=models.CASCADE)
    imagen = models.ImageField(max_length=1000, upload_to=image_path, null=True, blank=True)

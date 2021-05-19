import os
import uuid

from ckeditor.fields import RichTextField
from django.db import models, transaction
from django.utils.translation import gettext as _
from model_utils.models import TimeStampedModel


class HtmlWe(TimeStampedModel):
    def image_path(instance, filename):
        filename, file_extension = os.path.splitext(filename)
        ext = filename.split('.')[-1]
        name = "%s.%s" % (uuid.uuid4(), ext)
        return os.path.join(name + file_extension)

    class Meta:
        verbose_name = _('HTML Nosotros')
        verbose_name_plural = _('Contenido de nosotros')

    title = models.CharField(max_length=250, verbose_name='Titulo')
    description = RichTextField(verbose_name='Descripcion')
    cover_image = models.ImageField(max_length=1000, upload_to=image_path, null=True, blank=True,
                                    verbose_name='Imagen de portada')
    activate = models.BooleanField(default=True)

    @transaction.atomic
    def save(self, *args, **kwargs):
        HtmlWe.objects.filter(activate=True).update(activate=False)
        if self.id is not None:
            self.activate = True
        super().save(*args, **kwargs)


class We(TimeStampedModel):
    def image_path(instance, filename):
        filename, file_extension = os.path.splitext(filename)
        ext = filename.split('.')[-1]
        name = "%s.%s" % (uuid.uuid4(), ext)
        return os.path.join(name + file_extension)

    class Meta:
        verbose_name = _('Vision, Mision, Nosotros')
        verbose_name_plural = _('Vision, Mision, Nosotros')

    our_mission_title = models.CharField(max_length=100, verbose_name='Titulo Mision')
    our_mission_img = models.ImageField(max_length=1000, upload_to=image_path, null=True, blank=True,
                                        verbose_name='Imagen mision')
    our_mission_description = RichTextField(verbose_name='Descripcion mision')
    our_vision_title = models.CharField(max_length=100, verbose_name='Titulo Vision')
    our_vision_img = models.ImageField(max_length=1000, upload_to=image_path, null=True, blank=True,
                                       verbose_name='Imagen vision')
    our_vision_description = RichTextField(verbose_name='Descripcion vision')
    our_values_title = models.CharField(max_length=100, verbose_name='Titulo Valores')
    our_values_img = models.ImageField(max_length=1000, upload_to=image_path, null=True, blank=True,
                                       verbose_name='Imagen valores')
    our_values_description = RichTextField(verbose_name='Descripcion valores')
    activate = models.BooleanField(default=True)

    @transaction.atomic
    def save(self, *args, **kwargs):
        We.objects.filter(activate=True).update(activate=False)
        if self.id is not None:
            self.activate = True
        super().save(*args, **kwargs)

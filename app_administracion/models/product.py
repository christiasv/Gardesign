import os
import uuid

from ckeditor.fields import RichTextField
from django.db import models
from django.utils.translation import gettext as _
from model_utils.models import TimeStampedModel


class Category(TimeStampedModel):
    def image_path(instance, filename):
        filename, file_extension = os.path.splitext(filename)
        ext = filename.split('.')[-1]
        name = "%s.%s" % (uuid.uuid4(), ext)
        return os.path.join(name + file_extension)

    name = models.CharField(max_length=250, verbose_name='Nombre')
    description = models.CharField(max_length=250, blank=True, null=True, verbose_name='Desripción')
    cover_image = models.ImageField(max_length=1000, upload_to=image_path, null=True, blank=True,
                                    verbose_name='Imagen de portada')

    class Meta:
        verbose_name = _('Categoria')
        verbose_name_plural = _('Categorias')

    def __str__(self):
        return '{}'.format(self.name)


class Product(TimeStampedModel):
    def image_path(instance, filename):
        filename, file_extension = os.path.splitext(filename)
        ext = filename.split('.')[-1]
        name = "%s.%s" % (uuid.uuid4(), ext)
        return os.path.join(name + file_extension)

    name = models.CharField(max_length=250, verbose_name='Nombre')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name='Categoria')
    description = RichTextField(verbose_name='Descripcion', blank=True, null=True)
    cover_image = models.ImageField(max_length=1000, upload_to=image_path, null=True, blank=True,
                                    verbose_name='Imagen de portada')
    precio = models.FloatField(verbose_name='Precio del producto')
    more_info = models.CharField(max_length=750, blank=True, null=True, verbose_name='Hipervinculo (Ver más)')

    class Meta:
        verbose_name = _('Producto')
        verbose_name_plural = _('Productos')

    def __str__(self):
        return '{}'.format(self.name)


class GalleryImgProduct(models.Model):
    def image_path(instance, filename):
        filename, file_extension = os.path.splitext(filename)
        ext = filename.split('.')[-1]
        name = "%s.%s" % (uuid.uuid4(), ext)
        return os.path.join(name + file_extension)

    producto = models.ForeignKey(Product, related_name='gallery', on_delete=models.CASCADE)
    imagen = models.ImageField(max_length=1000, upload_to=image_path, null=True, blank=True)

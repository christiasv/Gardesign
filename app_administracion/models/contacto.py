from django.db import models
from django.utils.translation import gettext as _
from model_utils.models import TimeStampedModel


class Contacto(TimeStampedModel):
    name = models.CharField(max_length=250, verbose_name='Nombre')
    email = models.CharField(max_length=250, blank=True, null=True, verbose_name='Correo')
    subject = models.CharField(max_length=250, blank=True, null=True, verbose_name='Asunto')
    message = models.TextField(blank=True, null=True, verbose_name='Mensaje')

    class Meta:
        verbose_name = _('Contacto')
        verbose_name_plural = _('Contactos')

    def __str__(self):
        return '{}'.format(self.name)

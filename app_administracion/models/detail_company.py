from django.db import transaction, models
from django.utils.translation import gettext as _
from model_utils.models import TimeStampedModel


class DetailCompany(TimeStampedModel):
    direction = models.TextField(verbose_name='Dirección')
    # geolocation = models.PointField(help_text="Use map widget for point the house location")
    activate = models.BooleanField(default=True)

    class Meta:
        verbose_name = _('Detalle de empresa')
        verbose_name_plural = _('Detalle de empresa')

    def __str__(self):
        return '{}'.format(self.direction)

    @transaction.atomic
    def save(self, *args, **kwargs):
        DetailCompany.objects.filter(activate=True).update(activate=False)
        if self.id is not None:
            self.activate = True
        super().save(*args, **kwargs)

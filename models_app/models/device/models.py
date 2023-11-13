from django.db import models


class Device(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название устройства')
    verification_protocol = models.FileField(upload_to='protocols/', verbose_name='Протокол поверки')
    type = models.ForeignKey('Type', on_delete=models.CASCADE,
                             blank=True, null=True, verbose_name='Тип')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'devices'
        app_label = 'models_app'
        verbose_name = 'Устройство'
        verbose_name_plural = 'Устройства'

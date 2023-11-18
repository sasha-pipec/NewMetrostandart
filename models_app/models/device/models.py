from django.db import models


class Device(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    registry_number = models.ForeignKey('RegistryNumber', on_delete=models.CASCADE, verbose_name='Рег номер')
    type = models.ForeignKey('Type', on_delete=models.CASCADE, null=True, blank=True, verbose_name='Тип')

    def __str__(self):
        return f"{self.name} {self.registry_number} {self.type if self.type else '--' }"

    class Meta:
        db_table = 'devices'
        app_label = 'models_app'
        verbose_name = 'Устройство'
        verbose_name_plural = 'Устройства'

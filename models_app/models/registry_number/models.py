from django.db import models


class RegistryNumber(models.Model):
    number = models.CharField(max_length=100, verbose_name='Номер реестра')
    device = models.ForeignKey('Device', on_delete=models.CASCADE, verbose_name='Устройство')

    def __str__(self):
        return self.number

    class Meta:
        db_table = 'registry_numbers'
        app_label = 'models_app'
        verbose_name = 'Номер реестра'
        verbose_name_plural = 'Номера реестра'

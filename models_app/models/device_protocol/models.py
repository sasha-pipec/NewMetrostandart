from django.db import models


class DeviceProtocol(models.Model):
    device = models.ForeignKey('Device', on_delete=models.CASCADE, verbose_name='Устройство')
    protocol = models.ForeignKey('Protocol', on_delete=models.CASCADE, verbose_name='Протокол')

    def __str__(self):
        return f"{self.device.name} {self.protocol.name}"

    class Meta:
        db_table = 'device_protocols'
        app_label = 'models_app'
        verbose_name = 'Протокол устройтва'
        verbose_name_plural = 'Протоколы устройств'

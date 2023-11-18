from django.db import models


class Protocol(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    file = models.FileField(upload_to='protocols/', verbose_name='Файл')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'protocols'
        app_label = 'models_app'
        verbose_name = 'Протокол'
        verbose_name_plural = 'Протоколы'

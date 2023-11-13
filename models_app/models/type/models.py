from django.db import models


class Type(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название типа')
    subtype = models.ForeignKey('Subtype', on_delete=models.CASCADE,
                                blank=True, null=True, verbose_name='Подтип')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'types'
        app_label = 'models_app'
        verbose_name = 'Тип'
        verbose_name_plural = 'Типы'

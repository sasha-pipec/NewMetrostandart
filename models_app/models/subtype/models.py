from django.db import models


class Subtype(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название подтипа')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'subtypes'
        app_label = 'models_app'
        verbose_name = 'Подтип'
        verbose_name_plural = 'Подтипы'

from django.db import models


class Painting(models.Model):
    author = models.CharField(max_length=255, verbose_name='Автор росписи')
    painting = models.ImageField(upload_to='paintings/', verbose_name='Роспись')

    def __str__(self):
        return self.author

    class Meta:
        db_table = 'paintings'
        app_label = 'models_app'
        verbose_name = 'Роспись'
        verbose_name_plural = 'Росписи'

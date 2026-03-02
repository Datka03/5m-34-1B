from django.db import models

class Settings(models.Model):
    key = models.SlugField(
        unique=True,
        help_text="Уникальный ключ настройки, например site_name"
    )
    title = models.CharField(max_length=155, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание')
    is_public = models.BooleanField(default=False, verbose_name='Публичная настройка')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    def __str__(self):
        return self.key

    class Meta:
        verbose_name = 'Настройка'
        verbose_name_plural = 'Настройки'
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
from django.db import models

from relaxAPI.constants import CHAR_FIELD_DEFAULT_VALUE, TEXT_FIELD_DEFAULT_VALUE


class Post(models.Model):
    author = models.ForeignKey(
        verbose_name='Автор',
        to=User,
        on_delete=models.CASCADE,
        related_name='user_to_post',
        db_index=True
    )
    image = models.ImageField(
        verbose_name='Изображение',
        upload_to='posts',
        validators=[FileExtensionValidator(allowed_extensions=['png', 'jpg', 'jpeg'])]
    )
    title = models.CharField(verbose_name='Название', max_length=CHAR_FIELD_DEFAULT_VALUE)
    description = models.TextField(verbose_name='Описание', max_length=TEXT_FIELD_DEFAULT_VALUE)

    def __str__(self):
        return self.title

    def __repr__(self):
        return self.title

    class Meta:
        db_table = 'posts'

        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

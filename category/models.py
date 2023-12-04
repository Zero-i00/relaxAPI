from django.core.validators import FileExtensionValidator
from django.db import models

from post.models import Post
from relaxAPI.constants import CHAR_FIELD_DEFAULT_VALUE


class Category(models.Model):
    image = models.ImageField(
        verbose_name='Изображение',
        upload_to='categories',
        validators=[FileExtensionValidator(allowed_extensions=['png', 'jpg', 'jpeg'])]
    )
    title = models.CharField(verbose_name='Название', max_length=CHAR_FIELD_DEFAULT_VALUE)
    posts = models.ManyToManyField(
        verbose_name='Посты',
        to=Post,
        blank=True,
        related_name='posts_to_category',
        db_index=True
    )

    def __str__(self):
        return self.title

    def __repr__(self):
        return self.title

    class Meta:
        db_table = 'categories'

        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

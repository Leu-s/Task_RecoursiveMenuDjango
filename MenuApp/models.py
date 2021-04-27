from django.db import models
from django_extensions.db.fields import AutoSlugField
import re
from .utilities import slugify_function


class Category(models.Model):
    parent = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        related_name='child_category',
        verbose_name='Суперкатегорiя',
        on_delete=models.PROTECT
    )
    title = models.CharField(max_length=50, verbose_name='Назва')
    slug = AutoSlugField(populate_from='title', slugify_function=slugify_function)

    def __str__(self):
        name = f'{self.parent}/{self.title}'
        return re.sub('None/', '', name)

    class Meta:
        verbose_name = 'Категорія'
        verbose_name_plural = 'Категорії'
        ordering = ['title']


from django.contrib.auth import get_user_model
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.template.loader import render_to_string

from django.utils.text import slugify

from campings.fields import OrderField


class Place(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Camping(models.Model):
    owner = models.ForeignKey(get_user_model(), related_name='campings_creator', on_delete=models.CASCADE)
    place = models.ForeignKey('Place', related_name='campings', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    overview = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    regular = models.ManyToManyField(get_user_model(), related_name='camping_users', blank=True)
    camping_image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('-created',)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Type(models.Model):
    camp = models.ForeignKey('Camping', related_name='types', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, default='')
    order = OrderField(blank=True, for_fields=['camping'])

    def __str__(self):
        return f'{self.order}. {self.name}'

    class Meta:
        ordering = ['order']


class Content(models.Model):
    type = models.ForeignKey('Type', related_name='contents', on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, limit_choices_to={'model__in': (
        'text', 'video', 'image', 'file'
    )})
    object_id = models.PositiveIntegerField()
    item = GenericForeignKey('content_type', 'object_id')
    order = OrderField(blank=True, for_fields=['type'])

    class Meta:
        ordering = ['order']


class ItemBase(models.Model):
    owner = models.ForeignKey(get_user_model(), related_name='%(class)s_related', on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.title

    def render(self):
        return render_to_string(f'campings/content/{self._meta.model_name}.html', {'item': self})


class Text(ItemBase):
    content = models.TextField()


class File(ItemBase):
    content = models.FileField(upload_to='files')


class Image(ItemBase):
    content = models.ImageField(upload_to='content_images')


class Video(ItemBase):
    content = models.URLField()

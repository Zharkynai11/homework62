from django.db import models
from django.urls import reverse


class SoftDeleteManager(models.Manager):
    def active(self):
        return self.filter(is_deleted=False)

    def deleted(self):
        return self.filter(is_deleted=True)


class Category(models.Model):
    name = models.CharField(max_length=30,verbose_name="Название жанра")
    description = models.TextField(max_length=500, blank=True, null=True ,verbose_name="Описание")

class Movie(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=2000, null=True, blank=True)
    poster = models.ImageField(upload_to='posters', null=True, blank=True)
    release_date = models.DateField()
    finish_date = models.DateField(null=True, blank=True)
    is_deleted = models.BooleanField(default=False)
    category = models.ManyToManyField(Category,verbose_name="Жанр")
    objects = SoftDeleteManager()

    def get_absolute_url(self):
        return reverse('api_v1:movie-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name

class Hall(models.Model):
    name = models.CharField(max_length=30,verbose_name="Зал")

class Seat(models.Model):
    hall = models.ManyToManyField(Hall,verbose_name="Зал")
    raw = models.IntegerField(verbose_name="Номер ряда")
    pos = models.IntegerField(verbose_name="Номер места")

class Show(models.Model):
    movie = models.ManyToManyField(Movie,verbose_name="Фильм")
    hall = models.ManyToManyField(Hall,verbose_name="Зал")
    begin = models.DateTimeField(verbose_name="Начало")
    end = models.DateTimeField(verbose_name="Окончание")
    price = models.DecimalField(decimal_places = 2, max_digits=5, verbose_name="Цена")
# Create your models here.

from django.db import models
from django.db.models import Min,Max
from django.contrib import admin

class Students(models.Model):
    name = models.CharField(verbose_name = 'Имя', max_length=50)
    age = models.IntegerField(verbose_name='Возраст')

    class Meta:
        verbose_name_plural = 'Студенты'

    def __str__(self):
        return f'{self.name}'


class Different(models.Model):
    max_age = Students.objects.all().aggregate(Max('age'))
    

    def __str__(self):
        return f'{self.max_age}'

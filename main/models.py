from django.db import models


class Module(models.Model):

    title = models.CharField(max_length=50, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
# Create your models here.

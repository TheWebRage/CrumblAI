from django.db import models

# Create your models here.


class Cookie(models.Model):

    def __str__(self):
        return self.name

    name = models.CharField(max_length=50)
    attributes = models.ManyToManyField('Attribute')
    available = models.ManyToManyField('Available')


class Attribute(models.Model):

    attribute = models.CharField(max_length=50)


class Available(models.Model):

    available = models.DateField()


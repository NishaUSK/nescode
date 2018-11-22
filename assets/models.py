from django.conf import settings
from django.db import models
from django.utils import timezone


class Electronicgadgets(models.Model):
    name = models.CharField(max_length=200)
    model = models.TextField()
    prize = models.IntegerField(default=0)
    launch_date = models.DateTimeField(default=timezone.now)
    expiry_date = models.DateTimeField(blank=True, null=True)

    def expiry(self):
        self.expiry_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name


class Kitchen(models.Model):
    name = models.CharField(max_length=200)
    ingrediants = models.TextField()
    manufactured_date = models.DateTimeField(default=timezone.now)
    expiry_date = models.DateTimeField(blank=True, null=True)

    def expiry(self):
        self.expiry_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name


class Furnitures(models.Model):
    name = models.CharField(max_length=200)
    model = models.TextField()
    prize = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Plasticmaterials(models.Model):
    name = models.CharField(max_length=200)
    quality = models.TextField()
    prize = models.IntegerField(default=0)
    launch_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class Cars(models.Model):
    name = models.CharField(max_length=200)
    model = models.TextField()
    prize = models.IntegerField(default=0)
    launch_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

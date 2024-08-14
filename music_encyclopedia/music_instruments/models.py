from django.db import models


class Country(models.Model):
    country_name = models.CharField(max_length=255)
    flag_image = models.ImageField(upload_to='flags/', null=True, blank=True)


class People(models.Model):
    people_name = models.CharField(max_length=255)
    id_country = models.ForeignKey(Country, on_delete=models.CASCADE)


class Category(models.Model):
    category_title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='category_images/', null=True, blank=True)
    people = models.ForeignKey(People, on_delete=models.CASCADE, null=True)


class Instrument(models.Model):
    image = models.ImageField(upload_to='instrument_images/', null=True, blank=True)
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=3000)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

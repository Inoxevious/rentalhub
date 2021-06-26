from django.db import models
from django.shortcuts import reverse
from blog.models import Profile
import os
# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Property(models.Model):
    currrent_path = os.path.abspath(os.path.dirname('__file__')) + '/media/properties'

    class Meta:
        ordering = ["-publish_date"]

    owner = models.ForeignKey(Profile, on_delete=models.PROTECT)
    street = models.CharField(max_length=150, blank=True, null=True)
    city = models.CharField(max_length=150, blank=True, null=True)
    neighborhood = models.CharField(max_length=150, blank=True, null=True)
    short_description = models.CharField(max_length=150, blank=True, null=True)
    lease_rate = models.CharField(max_length=150, blank=True, null=True)
    description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    publish_date = models.DateTimeField(blank=True, null=True)
    published = models.BooleanField(default=False)
    meta_description = models.CharField(max_length=150, blank=True, null=True)
    tags = models.ManyToManyField(Tag, blank=True)
    slug = models.SlugField(max_length=255, unique=True)
    view_fee = models.FloatField(blank=True, null=True)
    image = models.ImageField(upload_to='media/properties', height_field=None, width_field=None, max_length=100)


    def get_absolute_url(self):
        return reverse("properties:property", kwargs={"slug": self.slug})

class PropertyImages(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, null=True, blank=True)
    front_image = models.ImageField(upload_to='media/properties')
    back_image = models.ImageField(upload_to='media/properties')
    side_image = models.ImageField(upload_to='media/properties')
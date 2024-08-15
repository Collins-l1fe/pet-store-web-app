from django.db import models
from datetime import datetime, date
from django.urls import reverse, reverse_lazy
from django.core.validators import MinValueValidator

class Collection(models.Model):
    title = models.CharField(max_length=255)
    #maincollection = models.ForeignKey(Collection, on_delete=models.PROTECT, blank=True, null=True)

    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering = ['title']

class product(models.Model):
    name = models.CharField(max_length=255)
    #description = RichTextField(blank=True, null=True)
    description = models.CharField(max_length=50000)
    Media = models.ImageField(blank=False, null=True, upload_to='static/images/productimages')
    price = models.DecimalField(max_digits=6, decimal_places=2, validators=[MinValueValidator(1)])
    inventory = models.IntegerField()
    last_update = models.DateTimeField(auto_now=True)
    collection = models.ForeignKey(Collection, on_delete=models.PROTECT, blank=True, null=True)
    listing_date = models.DateField(auto_now_add=True, null=True)
    type = models.CharField(max_length=155, null=True)
    brand = models.CharField(max_length=155, default='brand')
    feature1 = models.CharField(max_length=155, default='feature')
    feature2 = models.CharField(max_length=155, default='feature')
    feature3 = models.CharField(max_length=155, default='feature')
    feature4 = models.CharField(max_length=155, default='feature')
    def get_absolute_url(self):
        return reverse('page:dogproducts')
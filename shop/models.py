from django.db import models
from django.core.urlresolvers import reverse_lazy as reverse

# Create your models here.


class Catalog(models.Model):
    name = models.CharField(max_length=80)
    slug = models.SlugField(unique=True)
    parent = models.ForeignKey(
        'self', null=True, blank=True, related_name='children')
    image = models.ImageField(
        verbose_name=u'Image', upload_to="category_pic", blank=True)

    def __str__(self):              # __unicode__ on Python 2
        return self.name

    def get_absolute_url(self):
        return reverse('catalog_detail', kwargs={'slug': self.slug})


class Product(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    catalog = models.ForeignKey(Catalog)
    image = models.ImageField(
        verbose_name=u'Image', upload_to="product_pic", blank=True)
    description = models.TextField(blank=True, help_text="Describe product")
    video = models.URLField(blank=True, help_text="link from youtube")
    full_info = models.TextField(blank=True, help_text="Full information")
    price = models.DecimalField(max_digits=15, decimal_places=2)
    sale_price = models.DecimalField(
        max_digits=15, decimal_places=2, null=True)
    is_active = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)
    payment = models.CharField(max_length=200)
    delivery = models.CharField(max_length=200)
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):              # __unicode__ on Python 2
        return self.name

    def get_absolute_url(self):
        return reverse('shop_detail', kwargs={'slug': self.slug})

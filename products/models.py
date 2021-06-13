from blog.models import Category
from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100,)
    featured = models.BooleanField(default=False)

    class Meta:
        verbose_name = "categoría"
        verbose_name_plural = "categorías"
        ordering = ['id']
    
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name="Nombre")
    slug = models.SlugField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(verbose_name="Imagen", upload_to="productos/", null=True, blank=True)
    excerpt = models.TextField(max_length=200, verbose_name='Extracto')
    detail = models.TextField(max_length=500, verbose_name='Información del producto')
    price = models.FloatField()
    avialable = models.BooleanField(default=True)   

    class Meta:
        verbose_name = "producto"
        verbose_name_plural = "productos"
        ordering = ['id']

    def __str__(self):
        return self.name

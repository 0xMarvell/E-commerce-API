from django.db import models
from django.core.validators import MaxLengthValidator, MinLengthValidator

class Category(models.Model):
    title = models.CharField(max_length=150)

    def __str__(self):
        return self.title


class Books(models.Model):
    title = models.CharField(max_length=500)
    category = models.ForeignKey(Category, related_name='books', on_delete=models.CASCADE)
    isbn = models.PositiveIntegerField(validators=[MinLengthValidator(13), MaxLengthValidator(13)])
    pages = models.IntegerField()
    price = models.IntegerField()
    stock = models.IntegerField()
    description = models.TextField()
    image_url = models.URLField()
    status = models.BooleanField(default=True)
    created_on = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title


class Headphones(models.Model):
    product_tag = models.CharField(max_length=50)
    name = models.CharField(max_length=500)
    category = models.ForeignKey(Category, related_name='headphones', on_delete=models.CASCADE)
    price = models.IntegerField()
    stock = models.IntegerField()
    image_url = models.URLField()
    status = models.BooleanField(default=True)
    created_on = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f'{self.product_tag} {self.name}'

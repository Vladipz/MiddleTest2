from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Image(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='gallery_images/')
    categories = models.ManyToManyField(Category, blank=True)
    created_date = models.DateField()
    age_limit = models.PositiveIntegerField()

    def __str__(self):
        return self.title

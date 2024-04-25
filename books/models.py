from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    image = models.ImageField()
    description = models.TextField()
    price = models.PositiveIntegerField()
    published_time = models.DateField(auto_now_add=True)
    isbn = models.CharField(max_length=15)
    pages = models.PositiveIntegerField()

    def __str__(self):
        return self.title

from django.db import models

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(
        Author, max_length=100, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

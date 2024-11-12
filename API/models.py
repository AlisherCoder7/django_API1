from django.db import models


class Feature(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField()

    def __str__(self):
        return self.name

class FAQ(models.Model):
    question = models.CharField(max_length=300)
    answer = models.TextField()

    def __str__(self):
        return self.question

class News(models.Model):
    title = models.CharField(max_length=300)
    content = models.TextField()
    created_ad = models.DateTimeField(auto_now_add=True)
    updated_ad = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
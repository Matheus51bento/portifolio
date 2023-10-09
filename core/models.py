from django.db import models


class Tool(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Project(models.Model):

    title = models.CharField(max_length=200)
    description = models.TextField()
    overview = models.TextField()
    link = models.CharField(max_length=255)
    tools = models.ManyToManyField(Tool)

    def __str__(self):
        return self.title

from django.db import models


class Tool(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Project(models.Model):

    title = models.CharField(max_length=200)
    description = models.TextField()
    overview = models.TextField()
    link = models.CharField(max_length=255, null=True, blank=True)
    tools = models.ManyToManyField(Tool)
    tumb = models.ImageField(upload_to="projetos", null=True, blank=True)

    def __str__(self):
        return self.title


class Contact(models.Model):
    nome = models.CharField(max_length=300, verbose_name="Name")
    email = models.EmailField()
    mensage = models.TextField(verbose_name="Message")

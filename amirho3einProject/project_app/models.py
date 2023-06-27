from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField(blank=True)
    address = models.CharField(max_length=160)
    image = models.ImageField(upload_to="project")

    def __str__(self):
        return self.title

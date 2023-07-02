from django.db import models


class Services(models.Model):
    image = models.ImageField(upload_to="service")
    title = models.CharField(max_length=80)
    description = models.TextField()

    def __str__(self):
        return self.title

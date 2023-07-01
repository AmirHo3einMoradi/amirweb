from django.db import models


class Info(models.Model):
    name = models.CharField(max_length=50, blank=True)
    job = models.CharField(max_length=50, blank=True)
    bio = models.TextField(blank=True)
    prof = models.ImageField(upload_to='project', blank=True)
    address = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=50, blank=True)
    age = models.CharField(max_length=60, blank=True)
    Condition = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    email = models.EmailField()
    telegram = models.CharField(max_length=100)
    instagram = models.CharField(max_length=100)
    linkedin = models.CharField(max_length=100)
    github = models.CharField(max_length=100)


class Message(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    massage = models.TextField()

    def __str__(self):
        return f"{self.name} - {self.email}"



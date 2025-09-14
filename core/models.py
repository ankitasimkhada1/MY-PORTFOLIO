from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    skills = models.CharField(max_length=255)
    profile_picture = models.ImageField(upload_to='profiles/', blank=True)

    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    screenshot = models.ImageField(upload_to='projects/', blank=True)
    link = models.URLField(blank=True)

    def __str__(self):
        return self.title

class Testimonial(models.Model):
    quote = models.TextField()
    author = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.author} - {self.quote[:50]}"
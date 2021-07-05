from django.db import models


class Experience(models.Model):
    title = models.CharField(max_length=200)
    short_description = models.TextField()
    long_description = models.TextField()

    start_date = models.DateField()
    end_date = models.DateField(null=True)

    image = models.ImageField(upload_to='images/')
    technologies = models.ManyToManyField('Technology', blank=True)

    def __str__(self) -> str:
        return self.title


class Technology(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name

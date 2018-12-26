from django.db import models

class Opencons(models.Model):
    hyperlink = models.URLField()
    title = models.CharField(max_length=300)

    def __str__(self):
        return self.title

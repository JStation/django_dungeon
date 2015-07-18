from django.db import models

class Adventure(models.Model):
    title = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.title

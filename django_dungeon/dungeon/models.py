from django.db import models
from django.core.urlresolvers import reverse

class Adventure(models.Model):
    title = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('edit_adventure', args=[self.id])
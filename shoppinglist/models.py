from django.db import models

LEVEL_CHOICES = {
        'E': 'Empty',
        'L': 'Low',
        'F': 'Full',
    }

class Ingredient(models.Model):
    name = models.CharField(max_length=1024)
    level = models.CharField(max_length=1, choices=LEVEL_CHOICES.items())

    def __unicode__(self):
        return u'%s - %s' % (self.name, LEVEL_CHOICES[self.level])

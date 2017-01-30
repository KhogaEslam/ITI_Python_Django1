from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Track(models.Model):
    trName = models.CharField(max_length=200)

    def __str__(self):
        return self.trName

class Student(models.Model):
    stName = models.CharField(max_length=50)
    stAge = models.IntegerField()
    stTrack = models.ForeignKey(Track)

    def __str__(self):
        return self.stName

    def isBornBefore1992(self):
        return self.stAge > 25

    isBornBefore1992.short_description = 'Check Age'
    isBornBefore1992.boolean = True

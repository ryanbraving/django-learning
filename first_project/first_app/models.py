from django.db import models

# Create your models here.

#Topic :name of model (or database table)
class Topic(models.Model):  
    #top_name: class object attribute, represents a database field (column)
    top_name = models.CharField(max_length = 264, unique = True) 

    def __str__(self):
        return self.top_name

class Webpage(models.Model):
    topic = models.ForeignKey(Topic, on_delete = models.CASCADE)
    name = models.CharField(max_length = 264, unique = True)
    url = models.URLField(unique=True)

    def __str__(self):
        return self.name

class AccessRecord(models.Model):
    name = models.ForeignKey(Webpage, on_delete = models.DO_NOTHING)
    date = models.DateField()

    def __str__(self):
        return str(self.date)


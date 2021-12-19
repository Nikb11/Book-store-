from django.db import models
 
class Book(models.Model):
    title = models.CharField(max_length=50,null=False,blank=True)
    author = models.CharField(max_length=50,null=True)  
    price = models.IntegerField()
    category = models.CharField(max_length=40,null=True)


def __str__(self):
    return self.title    
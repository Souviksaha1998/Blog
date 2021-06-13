from django.db import models

# Create your models here.
class Blog(models.Model):
    name = models.CharField(max_length=40)
    subtitle = models.CharField(max_length=125)
    desc = models.CharField(max_length=255)
    
    date = models.DateTimeField(auto_now=False, auto_now_add=True , blank=True , null=True)

    def __str__(self):
        return self.name

   
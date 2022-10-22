from django.db import models

# Create your models here.
class Contact(models.Model):
    name= models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    subject = models.CharField(max_length=50)
    message = models.CharField(max_length=50)

    def __str__(self):
        return self.name

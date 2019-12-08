from django.db import models
from django.conf import settings

# Create your models here.
class Task(models.Model):
    description = models.CharField(max_length=200)
    
    category = models.ForeignKey('Category', 
                                 blank=True, null=True,
                                 on_delete=models.CASCADE)

    due = models.DateField()

    id = models.AutoField(primary_key=True)

    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE, 
                             blank=True, null=True)

    def __str__(self):
        return self.description

class Category(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "categories"       
 
    def __str__(self):        
        return self.name        

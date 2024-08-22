from django.db import models 
from django.contrib.auth.models import User


class Items(models.Model):
    date = models.DateField(null=True)
    description = models.TextField(null=True)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    category = models.CharField(max_length=100)
    
    
    def get_formatted_data(self):
        """Convert date to string"""
        if self.date:
            return self.date.strftime('%Y/%m/%d')
        return None
    
    
    def __str__(self):
        return (str(self.owner) + " " + str(self.get_formatted_data()) + " " + self.description[:50] + " " + self.category)
    
    
    class Meta:
        ordering = ['-date']
        
        
class Category(models.Model):
    name = models.CharField(max_length = 255)
    
    def __str__(self) -> str:
        return self.name
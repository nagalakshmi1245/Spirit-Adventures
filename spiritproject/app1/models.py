from django.db import models

# Create your models here.

class category(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name

class sub_category(models.Model):
    name=models.CharField(max_length=100)
    cid = models.ForeignKey(
        category, 
        on_delete=models.CASCADE, 
        blank=False,
        related_name='subcategories'
    )
    def __str__(self):
        return self.name

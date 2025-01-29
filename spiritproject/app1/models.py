from django.db import models

# Create your models here.
class userinfoModel(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    subject=models.CharField(max_length=150)
    message=models.CharField(max_length=150)

class feedback(models.Model):
    name=models.CharField(max_length=40)
    email=models.EmailField(max_length=40)
    feedback=models.CharField(max_length=200)

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

class contact(models.Model):
    first_name=models.CharField(max_length=150)
    last_name=models.CharField(max_length=150)
    email=models.EmailField(max_length=150)
    phone=models.IntegerField()
    address=models.CharField(max_length=150)
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
    

class Basecitypage(models.Model):
    city_name = models.CharField(max_length=100, unique=True)
    city_image=models.ImageField(upload_to='cityimages/')
    city_description=models.TextField()
    city_gallery1=models.ImageField(upload_to='cityimages/')
    city_gallery2=models.ImageField(upload_to='cityimages/')
    city_gallery3=models.ImageField(upload_to='cityimages/')
    city_gallery4=models.ImageField(upload_to='cityimages/')
    city_gallery5=models.ImageField(upload_to='cityimages/')
    city_map=models.ImageField(upload_to='cityimages/')
    
    def __str__(self):
        return self.city_name
    
class packages(models.Model):
    city = models.ForeignKey(Basecitypage, on_delete=models.CASCADE, related_name="packages",null=True, blank=True)
    package_image=models.ImageField(upload_to='images/')
    package_name=models.CharField(max_length=50)
    discount_price=models.IntegerField()
    full_price=models.IntegerField()
    Availability=models.CharField(max_length=25,null=True, blank=True)
    no_of_days=models.CharField(max_length=25)
    
    def __str__(self):
        return f"{self.package_name} - {self.city.city_name}"
    

class package_details_category(models.Model):
    day=models.CharField(max_length=100)
    def __str__(self):
        return self.day
    
class package_details_sub(models.Model):
    t1=models.CharField(max_length=100)
    t2=models.CharField(max_length=100)
    t3=models.CharField(max_length=100)
    t4=models.CharField(max_length=100)
    text=models.TextField()
    pid = models.ForeignKey(
        package_details_category, 
        on_delete=models.CASCADE, 
        blank=False,
        related_name='packagedetails'
    )
    # def __str__(self):
    #     return self.t1,self.t2,self.t3,self.t4,self.text
    


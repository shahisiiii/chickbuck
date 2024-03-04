from django.db import models

# Create your models here.



class Category(models.Model):
    category = models.CharField(max_length=50)
    category_image = models.ImageField(upload_to='images/',null=True)

    def __str__(self):
        return self.category
    
class Items(models.Model):
    name = models.TextField(max_length=100)
    description=models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    is_favourite = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    item_image = models.ImageField(upload_to='images/',null=True)


    def __str__(self):
        return self.name
from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class Category(models.Model):
    category = models.CharField(max_length=50,unique=True)
    category_image = models.ImageField(upload_to='images/',null=True)

    def __str__(self):
        return self.category
    
class Items(models.Model):
    item_name = models.TextField(max_length=100, unique = True)
    description=models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    is_favourite = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    item_image = models.ImageField(upload_to='images/',null=True)


    def __str__(self):
        return self.item_name
    
class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ForeignKey(Items,on_delete = models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.item_name} - {self.user.username}'s cart'"
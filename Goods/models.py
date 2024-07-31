from django.db import models 
from django.contrib.auth.models import User 
from random import sample 
import string 
 
class GenreateCode(models.Model): 
    generate_code = models.CharField(max_length=255, blank=True, unique = True, primary_key=True) 
    def save(self, *args, **kwargs): 
        if not self.generate_code: 
            self.generate_code = "".join(sample(string.ascii_letters, 20)) 
        super(GenreateCode, self).save(*args, **kwargs) 
         
         
    class Meta: 
        abstract = True 
         
         
         
 
class Banner(GenreateCode): 
    title = models.CharField(max_length=255) 
    sub_title = models.CharField(max_length=255, blank=True, null=True) 
    img = models.ImageField(upload_to='banners/') 
    is_active = models.BooleanField(default=True) 
 
    def __str__(self): 
        return self.title 
 
 
class Category(GenreateCode): 
    name = models.CharField(max_length=255) 
    generate_code = models.CharField(max_length=255, blank=True, unique=True) 
    imges = models.ImageField() 
     
     
 
    def __str__(self): 
        return self.name 
 
    def save(self, *args, **kwargs): 
        if not self.generate_code and not self: 
            self.generate_code = "".join(sample(string.ascii_letters, 20)) 
        super(Category, self).save(*args, **kwargs) 
 

class Product(GenreateCode): 
    name = models.CharField(max_length=255) 
    quantity = models.PositiveIntegerField(default=1) 
    price = models.DecimalField(max_digits=8, decimal_places=2) 
    category = models.ForeignKey(Category, on_delete=models.CASCADE) 
    description = models.TextField() 
 
    def __str__(self): 
        return self.name 
     

class ProductEnter(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField()
    old_quantity = models.IntegerField(blank=True, null=True, default=0)
    date = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
     
    def save(self, *args, **kwargs):
        if not self.id:
            self.old_quantity = self.product.quantity
            self.product.quantity += self.quantity
        else:
            original = ProductEnter.objects.get(generate_code=self.generate_code)
            if self.product:
                self.product.quantity -= original.quantity
                self.product.quantity += self.quantity

        self.product.save()
        super().save(*args, **kwargs)
         
    def __str__(self):
        return self.product.name
 
 
class ProductImg(models.Model): 
    product = models.ForeignKey(Product, on_delete=models.CASCADE) 
    img = models.ImageField(upload_to='product-img') 
 
    def __str__(self): 
        return self.product.name 
 

class Cart(models.Model): 
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True) 
    is_active = models.BooleanField(default=True) 
    shopping_date = models.DateTimeField(blank=True, null=True) 
 
    def __str__(self): 
        return self.author.username 
 

class CartProduct(models.Model): 
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True) 
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE) 
    quantity = models.PositiveIntegerField(default=1) 
 
    def __str__(self): 
        return self.product.name 
 

class Order(GenreateCode): 
    cart = models.ForeignKey(Cart, on_delete=models.SET_NULL, null=True) 
    full_name = models.CharField(max_length=255) 
    email = models.EmailField(blank=True, null=True) 
    phone = models.CharField(max_length=13) 
    address = models.CharField(max_length=255) 
    status = models.SmallIntegerField( 
        choices=( 
            (1, 'Tayyorlanmoqda'), 
            (2, 'Yo`lda'), 
            (3, 'Yetib borgan'), 
            (4, 'Qabul qilingan'), 
            (5, 'Qaytarilgan'), 
        ) 
    ) 
 
    def __str__(self): 
        return self.full_name
    
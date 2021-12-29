from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField
# Create your models here.

class Categories(models.Model):
    name = models.CharField(max_length=200)
    
    
    def __str__(self):
        return self.name
    
    
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = 'Categories'
        ordering = ('id',)
    
    
class Brand(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Brand"
        verbose_name_plural = 'Brands'
        ordering = ('id',)

    
class Color(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Color"
        verbose_name_plural = 'Colors'
        ordering = ('id',)


class Price_Filter(models.Model):
    
    FILTER_PRICE = (
        ('1 - 10', '1 - 10'),
        ('10 - 100', '10 - 100'),
        ('100 - 300', '100 - 300'),
        ('300 - 500', '300 - 500'),
        ('500 - 1000', '500 - 1000'),
        ('Over 1000', 'Over 1000'),
    )
    
    price = models.CharField(choices=FILTER_PRICE, max_length=60)
    
    
    def __str__(self):
        return self.price
    
    
    class Meta:
        verbose_name = "Price Filter"
        verbose_name_plural = 'Price Filters'
        ordering = ('id',)



class Product(models.Model):
    
    CONDITION = (
        ('New', 'New'),
        ('Used', 'Used')
    )
    
    STOCK_CHOICES = (
        ('IN STOCK', 'IN STOCK'),
        ('OUT OF STOCK', 'OUT OF STOCK')
    )
    
    STATUS_CHOICES = (
        ('Published', 'Published'),
        ('Draft', 'Draft')
    )
    
    unique_id       = models.CharField(unique=True, max_length=200, null=True, blank=True)
    image           = models.ImageField(upload_to='uploads/products', default='No-image-available.jpg')
    name            = models.CharField(max_length=200)
    price           = models.DecimalField(max_digits=10, decimal_places=2)
    condition       = models.CharField(choices=CONDITION, max_length=100)
    information     = RichTextField(null=True)
    description     = RichTextField(null=True)
    stock           = models.CharField(choices=STOCK_CHOICES, max_length=200)
    status          = models.CharField(choices=STATUS_CHOICES, max_length=200)
    created_date    = models.DateTimeField(default=timezone.now)
    
    categories      = models.ForeignKey(Categories, on_delete=models.CASCADE)
    brand           = models.ForeignKey(Brand, on_delete=models.CASCADE)
    color           = models.ForeignKey(Color, on_delete=models.CASCADE)
    price_filter    = models.ForeignKey(Price_Filter, on_delete=models.CASCADE)
    
    
    def save(self, *args, **kwargs):
        if self.unique_id is None and self.created_date and self.id:
            self.unique_id = self.created_date.strftime('75%Y%m%d23') + str(self.id)
        return super().save(*args, **kwargs)

    
    def __str__(self):
        return self.name
    
    
    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ('id',)
        
        

class Images(models.Model):
    image = models.ImageField(upload_to='uploads/products')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.product)

    class Meta:
        verbose_name = 'Image'
        verbose_name_plural = 'Images'
        ordering = ('id',)

    
    
class Tag(models.Model):
    name = models.CharField(max_length=200)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'
        ordering = ('id',)

from django.db import models

class Product(models.Model):
    title = models.CharField('Title', max_length=50, blank=True, null=True)
    description = models.CharField('Description', max_length=250, blank=True, null=True)
    category = models.CharField('Category', max_length=20, blank=True, null=True)
    price = models.DecimalField('Price', max_digits=10, decimal_places=2, blank=True, null=True)
    discountPercentage = models.DecimalField('Discount Percentage', max_digits=6, decimal_places=2, blank=True, null=True)
    rating = models.DecimalField('Rating', max_digits=6, decimal_places=2, blank=True, null=True)
    stock = models.DecimalField('Stock', max_digits=5, decimal_places=0, blank=True, null=True)
    brand = models.CharField('Brand', max_length=15, blank=True, null=True)
    sku = models.CharField('SKU', max_length=20, blank=True, null=True)
    weight = models.DecimalField('Weight', max_digits=5, decimal_places=0, blank=True, null=True)
    warrantyInformation = models.CharField('Warranty Information', max_length=25, blank=True, null=True)
    shippingInformation = models.CharField('Shipping Information', max_length=50, blank=True, null=True)
    availabilityStatus = models.CharField('Availability Information', max_length=10, blank=True, null=True)
    returnPolicy = models.CharField('Return Policy', max_length=25, blank=True, null=True)
    minimumOrderQuantity = models.DecimalField('Minimum Order Quantity', max_digits=5, decimal_places=0, blank=True, null=True)
    thumbnail = models.CharField('Thumbnail', max_length=200, blank=True, null=True)

    def __str__(self):
        return self.title
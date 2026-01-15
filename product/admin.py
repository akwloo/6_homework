from django.contrib import admin
from . models import Product
from import_export.admin import ImportExportModelAdmin
from .resources import ProductResource

class ProductAdmin(ImportExportModelAdmin):
  list_display = ("title", "description", "category", "price", "discountPercentage", "rating", "stock", "brand", "sku", "weight", 
                  "warrantyInformation", "shippingInformation", "availabilityStatus", "returnPolicy", "minimumOrderQuantity", "thumbnail",)
  resource_class = ProductResource

admin.site.register(Product, ProductAdmin)
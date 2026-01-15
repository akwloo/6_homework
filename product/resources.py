from import_export import resources
from .models import Product

class ProductResource(resources.ModelResource):

    def before_import(self, queryset, **kwargs):
        Product.objects.all().delete()
        super().before_import(queryset, **kwargs)

    def before_import_row(self, row, **kwargs):
        row["title"] = f"{str(row['title']):.{50}}"
        row["description"] = f"{str(row['description']):.{250}}"
        row["category"] = f"{str(row['category']):.{20}}"
        row["price"] = f"{float(row['price']):.{10}}"
        row["discountPercentage"] = f"{float(row['discountPercentage']):.{6}}"
        row["rating"] = f"{float(row['rating']):.{6}}"
        row["stock"] = f"{float(row['stock']):.{5}}"
        row["brand"] = f"{str(row['brand']):.{15}}"
        row["sku"] = f"{str(row['sku']):.{20}}"
        row["weight"] = f"{float(row['weight']):.{5}}"
        row["warrantyInformation"] = f"{str(row['warrantyInformation']):.{25}}"
        row["shippingInformation"] = f"{str(row['shippingInformation']):.{50}}"
        row["availabilityStatus"] = f"{str(row['availabilityStatus']):.{10}}"
        row["returnPolicy"] = f"{str(row['returnPolicy']):.{25}}"
        row["minimumOrderQuantity"] = f"{float(row['minimumOrderQuantity']):.{5}}"
        row["thumbnail"] = f"{str(row['thumbnail']):.{200}}"
        super().before_import_row(row, **kwargs)

    def after_export(self, queryset, data, **kwargs):
        Product.objects.all().delete()
        super().after_export(queryset, data, **kwargs)

    class Meta:
        model = Product

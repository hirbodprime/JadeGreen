from django.contrib import admin
from .models import CategoryModel , SubCategoryModel , ProductModel


admin.site.register(CategoryModel)
admin.site.register(SubCategoryModel)
admin.site.register(ProductModel)
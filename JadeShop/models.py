from django.db import models
from utils.models import BaseModel
import random
from utils.functions import get_filename_ext


def upload_image_path(instance, filename):
    new_name = random.randint(1, 27634723542)
    name, ext = get_filename_ext(filename)
    final_name = f"{new_name}-{instance.name}{ext}"
    return f"product/{final_name}" 


class CategoryModel(BaseModel):
    def __str__(self):
        return self.name


class SubCategoryModel(BaseModel):
    Category = models.ForeignKey(CategoryModel , on_delete=models.CASCADE)
    def __str__(self):
        return self.name


class ProductModel(BaseModel):
    image = models.ImageField(upload_to=upload_image_path)
    price = models.CharField(max_length=30)
    date = models.DateTimeField(auto_now_add=True)
    discription = models.TextField(max_length=600)
    offer = models.CharField(max_length=30)
    special = models.BooleanField(default=False)
    deleted = models.BooleanField(default=False)
    def __str__(self):
        return self.name

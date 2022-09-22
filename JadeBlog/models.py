from django.db import models
from utils.models import BaseModel
from django.contrib.auth import get_user_model 
import random
from utils.functions import get_filename_ext


User = get_user_model()


def upload_image_path(instance, filename):
    new_name = random.randint(1, 27634723542)
    name, ext = get_filename_ext(filename)
    final_name = f"{new_name}-{instance.name}{ext}"
    return f"blog/{final_name}" 


class BlogModel(BaseModel):
    owner = models.ForeignKey(User , on_delete=models.CASCADE)
    image = models.ImageField(upload_to=upload_image_path )
    discription = models.TextField(max_length=600)
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

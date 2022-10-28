from django.db import models
from utils.models import BaseModel
import random
from utils.functions import get_filename_ext




def upload_image_path(instance, filename):
    new_name = random.randint(1, 27634723542)
    name, ext = get_filename_ext(filename)
    final_name = f"{new_name}-{instance.name}{ext}"
    return f"Activity/{final_name}" 


class ActivitiesModel(BaseModel):
    image = models.ImageField(upload_to=upload_image_path, null=True , blank=True)
    discription = models.TextField(max_length=600)
    def __str__(self):
        return self.name
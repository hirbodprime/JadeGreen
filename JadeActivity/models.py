from django.db import models
from utils.models import BaseModel

class ActivitiesModel(BaseModel):
    discription = models.TextField(max_length=600)
    def __str__(self):
        return self.name
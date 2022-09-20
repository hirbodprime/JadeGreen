from .models import CustomUser
from django.db.models.signals import post_save
from django.core.validators import validate_email
from django.forms import ValidationError

def updateUser(sender, instance, **kwargs):
    user = instance
    print(user.password2)
post_save.connect(updateUser, sender=CustomUser)
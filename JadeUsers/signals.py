from django.db.models.signals import post_save , pre_save
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
import random
from django.conf import settings
from rest_framework.authtoken.models import Token

UserModel = get_user_model()

def updateUser(sender, instance, **kwargs):
    anonymousUser = random.randint(0 , 234124)
    user = instance
    if user.password2 != user.password:
        user.password2 = user.password
    user.password2 = make_password(user.password2)
    if not user.first_name and not user.last_name:
        user.first_name = "anonymousUser"
        user.last_name = f"{anonymousUser}-{user.id}"
        user.fullname = f"{user.first_name}-{user.last_name}"
    if not len(user.password) == 88: # lenght of hashed plain text is 88
        user.password = make_password(user.password)
pre_save.connect(updateUser, sender=UserModel)



def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
post_save.connect(create_auth_token,sender=UserModel)
from django.db.models.signals import post_save , pre_save
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password

UserModel = get_user_model()

def updateUser(sender, instance, **kwargs):
    user = instance
    user.password2 = make_password(user.password2)
pre_save.connect(updateUser, sender=UserModel)
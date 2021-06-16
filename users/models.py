import functools
from django.db import models

from datetime import datetime, timedelta

from . import auth

import uuid
from functools import wraps

# Create your models here.

def username_validation(username):
    user = Users.objects.filter(username=username).first()
    if user:
        print("User Exists")
        return False
    return True

def user_exists(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        print(args, "\n")
        print(kwargs)
        object, *data = args
        if username_validation(getattr(object, "username")):
            function(*args, **kwargs)
        else:
            raise TypeError("Method called on existing user")
    return wrapper

def existing_user(function):
    def wrapper(*args, **kwargs):
        object, *data = args
        if username_validation(getattr(object, "username")):
            function(*args, **kwargs)
        else:
            raise Exception("Method Called on Non-Existing User")






def user_authenticate(login_info, login_password):

    user_data = Users.objects.filter(username=login_info).first()
    if user_data:
        if auth.checkPasswd(login_password, user_data.password):
            pass
    pass


class Users(models.Model):
    uid= models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=24, default='')
    email = models.EmailField(default='')
    password = models.BinaryField(max_length=1000, default=b'')
    created_on = models.DateField(default=datetime.now, editable=False)
    user_data = models.JSONField(default=dict, encoder=None, decoder=None)


    @user_exists
    def create_user(self):
        self.username = self.username.lower()
        self.user_data = {
            "personal_data": {
                "firstName": "",
                "lastName": "",
                "birthday": "",
            },
            "card_data": [],
            "companion":[],
        }
        self.password = auth.hashPasswd(self.password)
        self.save()
    
    @existing_user
    def update_user(self, data_to_update: dict) -> None:
        keys = data_to_update.keys()
        try:
            for key in keys:
                if hasattr(self, key):
                    if key == "password":
                        data_to_update[key] = auth.hashPasswd(data_to_update[key])
                    setattr(self, key, data_to_update[key])
            self.save()
        except:
            print("Could Not Update User")

    @existing_user
    def delete_user(self):
        self.delete()

# class UserData(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
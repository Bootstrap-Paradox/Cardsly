from sys import exec_prefix
import bcrypt as bc
from django.contrib.auth import login
from django.db.models.query import QuerySet



import re


class Authenticate:

    def __init__(self):
        self.packet = (False, {}, "User Not Found")
        pass

    def hashPasswd(self, password):
        return bc.hashpw(bytes(password, "utf-8"), bc.gensalt())

    def checkPasswd(self, password, hashed_password):
        password = bytes(password, "utf-8")
        print(password)
        return bc.checkpw(password, hashed_password)

    def sign_up_user(self, username: str, email: str, password: str) -> tuple:

        try:
            from .models import Users

            user = Users(username=username, email=email, password=password)
            user.create_user()
            self.packet = (True, user, "SignUp Successful")

        except Exception as err:
            print(err)
        
        return self.packet


    def login_user(self, login_text: str, password: str) -> tuple:

        try:
            from .models import Users

            email_regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'
            user_data = Users.objects.filter(email=login_text) if re.search(email_regex, login_text) else Users.objects.get(username=login_text)

            # print(type(user_data))
            if isinstance(user_data, QuerySet):

                for data in user_data:
                    self.packet = self.auth_user_password(data, password)
                    logged_in, data, message = self.packet
                    if logged_in:
                        break

            elif user_data:

                self.packet =  self.auth_user_password(user_data, password)


        except Exception as err:
            print(err)

        return self.packet

    def auth_user_password(self, user_data, password, message_keyword="Login"):

        password_auth = self.checkPasswd(password, user_data.password)
        return (password_auth, user_data, f"{message_keyword} Successful" if password_auth else "Password Invalid")





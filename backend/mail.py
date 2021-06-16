from django.core.mail import send_mail


class Mailing_system:
    def __init__(self) -> None:
        pass

    def welcome_email(self):
        print("sending Mail Test")
        # send_mail(
        #     "Welcome Email",
        #     "Thank you for joining us, Let's Have some fun",
        #     "siddhantkuchnure27@gmail.com",
        #     ["sidkuchnure@gmail.com"],
        #     fail_silently=False,
        #     auth_password="27siddhant2002"
        # )


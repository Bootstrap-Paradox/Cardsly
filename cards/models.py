from django.db import models

from datetime import datetime, timedelta, date

import uuid

from django.utils.translation import deactivate


# Create your models here.

def create_expiry_date(days):
    return datetime.now() + timedelta(days=2)

def get_card_from_uid(uid:str) -> tuple:
    print(type(uid))
    # uid = uuid.UUID(uid)
    # print(type(uid))
    card: Card
    packet = ()
    try:
        card:Card = Card.objects.get(uid=uid)
        print(card)
            
        if date.today() >= card.expires_on:
            card.delete()
            packet =  (False, {}, "Card Expired")
        else:
            packet =  (True, {
            "uid": card.uid,
            "senderName":card.senderName,
            "receiverName": card.recieverName,
            "message": card.message,
            "custom_message": card.custom_message,
            "cardType": card.image_name,
            "expires_on": card.expires_on,
            "heart_activated": card.heart_activated
        }, "")

    except:
        packet = (False, {}, "Card Not Found")

    print(packet, "\n")

    return packet

class Card(models.Model):

    uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    senderName = models.CharField(max_length=250, default='', blank=True)
    recieverName = models.CharField(max_length=250, default='', blank=True)
    message = models.TextField(default='', blank=True, null=True)
    custom_message = models.TextField(default='', blank=True, null=True)
    image_name = models.CharField(max_length=500, default='', blank=False)
    heart_activated = models.BooleanField(default=False, blank=False, null=False)
    created_on = models.DateField(default=datetime.now)
    expires_on = models.DateField(null=True)

    def create_card(self, max_days=2, message="", custom_message="", senderName="", recieverName="", image_name="get_well_soon", host=""):
        self.expires_on = datetime.now() + timedelta(days=max_days) if max_days < 30 else datetime.now() + timedelta(days=4)
        self.message = message
        self.custom_message = custom_message
        self.senderName = senderName
        self.recieverName = recieverName
        self.image_name = image_name

        self.save()


        return self.__build_url(host)

    def __build_url(self, host):
        return f"/cards/{str(self.uid)}"


    def get_card_from_uid(self, uid:str) -> tuple:
        print(type(uid))
        # uid = uuid.UUID(uid)
        # print(type(uid))
        card: Card
        packet = ()
        try:
            card:Card = Card.objects.get(uid=uid)
            print("card", card)
                
            if date.today() >= card.expires_on:
                card.delete()
                packet =  (False, {}, "Card Expired")
            else:
                packet =  (True, {
                "uid": card.uid,
                "senderName":card.senderName,
                "receiverName": card.recieverName,
                "message": card.message,
                "custom_message": card.custom_message,
                "cardType": card.image_name,
                "expires_on": card.expires_on,
                "heart_activated": card.heart_activated
            }, "")

        except Exception as e:
            print(e)
            packet = (False, {}, "Card Not Found")

        print(packet, "\n")

        return packet

    
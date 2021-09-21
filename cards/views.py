
from django.http.response import HttpResponseRedirect, HttpResponse
from django.shortcuts import redirect, render
from .models import get_card_from_uid, Card
from .forms import CreateCard

from beautifulCards.backend.mail import Mailing_system

# from backend.mail import Mailing_system

from .backend.layout import LayoutGenerator

from django.http import JsonResponse

# Create your views here.

layout = LayoutGenerator()


def heart_update_api(response: dict, cardUID, param=""):
    print(cardUID)
    valid, data, error_message = Card().get_card_from_uid(cardUID)
    response_data: dict
    if valid:
        print("valid")
        card: Card = Card.objects.get(uid=cardUID)
        if param == "update":
            print("update")
            card.heart_activated = not data["heart_activated"]
            card.save()
            response_data = {
                "heart_activated": not data["heart_activated"]
            }
        elif param == "fetch":
            print("fetch")
            # data["heart_activated"] = card.heart_activated
            response_data = {
                "heart_activated": data["heart_activated"]
            }
        else:
            response_data = {
                "error": "Parameter Invalid"
            }
    else:
        response_data = {
            "error": "card Invalid"
        }
    return JsonResponse(response_data)


def getWellSoon(response: dict) -> render:
    return render(response, "cards/getWellSoon.html", {})


def display_custom_card(response, cardUID: str) -> render:
    valid, data, error_message = Card().get_card_from_uid(cardUID)
    if not valid:
        return render(response, "main/error.html", {"error_message": error_message})

    print("\n\n", data)
    # message: str = "This is a Message that is generated when you create a card so even if you don't have a custom message to convey your feelings we will do that for you, all because we care about Relations"
    svg_image = layout.fetch_svg(data["cardType"])
    data["svg_image"] = svg_image
    return render(response, "cards/displayCustomCard.html", data)


def create_card(response: dict) -> render:
    if response.method == "POST":
        form = CreateCard(response.POST)

        if form.is_valid():
            senderName = form.cleaned_data["senderName"]
            receiverName = form.cleaned_data["receiverName"]
            custom_message = form.cleaned_data["custom_message"]
            toggle_random_generator = form.cleaned_data.get(
                "toggle_random_generator", False)
            cardType = form.cleaned_data["cardType"]
            message = layout.generate_message(
                cardType) if toggle_random_generator else ""
            print(message)
            card = Card()
            card_url = card.create_card(
                message=message,
                custom_message=custom_message,
                senderName=senderName,
                recieverName=receiverName,
                image_name=cardType,
                host=response.META['HTTP_HOST']
            )
            print(card_url)
            return redirect(card_url)

    else:
        form = CreateCard()
    return render(response, "cards/createCard.html", {"form": form})


def selectCard(response: dict) -> render:

    items = [
        {
            "name": "Get Well Soon",
            "url": "/get-well-soon"
        },
        {
            "name": 'Happy Birthday',
            "url": '/'
        }
    ]
    return render(response, "cards/selectCard.html", {"items": items})

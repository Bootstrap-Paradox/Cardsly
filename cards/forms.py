from typing import Pattern
from django import forms
from django.db.models.enums import Choices
from django.forms.widgets import TextInput

class CreateCard(forms.Form):
    senderName = forms.CharField(widget=forms.TextInput(attrs={
        "placeholder": "Who's Sending",
        "autocomplete": "off",
        "type": "text",
        "name": "senderName"

    }), required=False,
    label="")

    receiverName = forms.CharField(widget=forms.TextInput(attrs={
        "placeholder": "Who's Receiving",
        "autocomplete": "off",
        "type": "text",
        "name": "receiverName"

    }), required=False,
    label="")


    custom_message = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "placeholder": "Your Special Message",
                "autocomplete": "off",
                "name": "custom_message"
            }
        ),
        required=False,
        label=""
    )

    toggle_random_generator = forms.BooleanField(label="Generate Random Message", required=False, widget=forms.CheckboxInput(attrs={"checked": True}), show_hidden_initial=True)

    

    cardType = forms.CharField(
        widget=forms.Select(
            attrs={"name": "cardType"}
            ,choices=(
        ("birthday", "Happy Birthday"),
        ("get_well_soon", "Get Well Soon"),
        ("missing_you", "Missing You")
    )
        ),
        label=""
    )

    def clean_custom_message(self):
        toggle = self.data.get("toggle_random_generator", False)
        print(f"\nThis is a Toggle to generate Message: {toggle}")
        if not toggle and self.data["custom_message"] == "":
            raise forms.ValidationError("Can't Create an Empty Page")

        return self.data["custom_message"]



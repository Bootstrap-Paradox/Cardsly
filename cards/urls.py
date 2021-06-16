from django.urls import path, re_path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views

urlpatterns = [
    
    path("get-well-soon", views.getWellSoon, name="getWellSoon"),
    path("create-card", views.create_card, name="createCard"),
    path("api/<str:cardUID>+<str:param>", views.heart_update_api, name="heartUpdateApi"),
    path("<str:cardUID>",views.display_custom_card, name="displayCustomCard")
]


from django.urls import path
from .views import Main
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', Main.as_view()),
]

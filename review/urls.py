
from django.urls import path
from . import views

urlpatterns = [
    path("", views.ReviewView.as_view()),
    path("thank_u",views.thank_u),
]
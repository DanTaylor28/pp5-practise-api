from django.urls import path
from pins import views

urlpatterns = [
    path('pins/', views.PinList.as_view()),
]

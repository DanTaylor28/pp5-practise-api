from django.urls import path
# from .views import ProfileList
from profiles import views

urlpatterns = [
    path('profiles/', views.ProfileList.as_view()),
]

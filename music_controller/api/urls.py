from django.urls import path
from .views import main, RoomView
 
urlpatterns = [
    path('home', main),
    path('', main),
    path('view', RoomView.as_view())
]
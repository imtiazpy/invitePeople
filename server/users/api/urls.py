from django.urls import path

from .views import UserActivationView


app_name = 'Users'


urlpatterns = [
    path('activate/<str:uid>/<str:token>', UserActivationView.as_view())
]

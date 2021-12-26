
from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from AuthEngine.views import Register

urlpatterns = [
    path('v1/register', csrf_exempt(Register.as_view()),name="AuthEngine_Register_v1"),
]

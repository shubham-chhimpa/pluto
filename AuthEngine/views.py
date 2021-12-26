from django.shortcuts import render

# Create your views here.
from django.views.generic.base import View
from django.http.response import JsonResponse

from AuthEngine.responses import send_200


class Register(View):

    def __init__(self, **kwargs):
        super().__init__(kwargs)
        self.response = None

    def dispatch(self, *args, **kwargs):
        return super(Register, self).dispatch(*args, **kwargs)

    def post(self, request):

        print(request)
        self.response = {
            "message": "working"
        }

        return send_200(self.response)

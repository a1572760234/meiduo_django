from django.shortcuts import render
from django.views import View
from apps.users.models import User
from django.http import JsonResponse

# Create your views here.

class UsernameCountView(View):
    def get(self, request, username):
        count = User.objects.filter(username=username).count()

        return JsonResponse({'code': 0,'errmsg': 'ok', 'count': count})
from django.shortcuts import render
from django.http.response import JsonResponse
from django.views import View


class Index(View):
    def get(self, request):
        print(request)
        return JsonResponse({1: 1})
    # return render(request, "chat/template/chat/index.html")

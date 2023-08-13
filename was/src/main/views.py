from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.views import APIView

class Main(APIView):
    def get(self, request):
        context = {}
        context['title'] = '게시판 홈'
        return render(request, 'home.html', context)

    def post(self, request):
        return render(request, 'home.html')

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def hello_world(request):
    # return HttpResponse('Hello World!') #단순 문자열 출력
    return render(request, 'accountapp/hello_world.html') # 함수인자, 만든 html 불러오기

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def hello_world(request):
    # return HttpResponse('Hello World!') #단순 문자열 출력
    # 메서드 분류 해서 출력 위해 if 사용 (get, post)
    if request.method == "POST":
        temp = request.POST.get('input_text')

        return render(request, 'accountapp/hello_world.html',
                      context={'text': temp})
    else:
        return render(request, 'accountapp/hello_world.html',
                      context={'text': 'GET METHOD'})

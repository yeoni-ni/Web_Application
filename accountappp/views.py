from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from accountappp.models import HelloWorld


def hello_world(request):
    # return HttpResponse('Hello World!') #단순 문자열 출력
    # 메서드 분류 해서 출력 위해 if 사용 (get, post)
    if request.method == "POST":

        temp = request.POST.get('input_text')

        new_hello_world=HelloWorld()
        new_hello_world.text = temp
        new_hello_world.save()

        # DB읽어오기(클래스 안 모든 오브젝트 불러오기)
        hello_world_list = HelloWorld.objects.all()


        return render(request, 'accountapp/hello_world.html',
                      context={' hello_world_list': hello_world_list }) # 객체반환
    else:
        hello_world_list = HelloWorld.objects.all()
        return render(request, 'accountapp/hello_world.html',
                      context={'hello_world_list': hello_world_list})

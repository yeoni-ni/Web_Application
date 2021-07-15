from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView

from accountapp.models import HelloWorld


def hello_world(request):
    # return HttpResponse('Hello World!') #단순 문자열 출력
    # 메서드 분류 해서 출력 위해 if 사용 (get, post)
    if request.method == "POST":

        temp = request.POST.get('input_text')

        new_hello_world=HelloWorld()
        new_hello_world.text = temp
        new_hello_world.save()

        # 재연결
        return HttpResponseRedirect(reverse('accountapp:hello_world'))

    else:
        hello_world_list = HelloWorld.objects.all()
        return render(request, 'accountapp/hello_world.html',
                      context={'hello_world_list': hello_world_list })


class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/create.html'
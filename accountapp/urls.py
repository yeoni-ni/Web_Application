from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from accountapp.views import hello_world, AccountCreateView, AccountDetailView

app_name ='accountapp'

urlpatterns = [
    path('hello_world/', hello_world, name="hello_world"),
    # 로그인
    path('login/',LoginView.as_view(template_name='accountapp/login.html'),name='login'),
    # 로그아웃
    path('logout/',LogoutView.as_view(),name='logout'),
    # 회원가입
    path('create/',AccountCreateView.as_view(),name='create'),
    # Detail
    path('detail/<int:pk>', AccountDetailView.as_view(), name='detail')

]

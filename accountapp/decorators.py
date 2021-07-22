# 계정의 소유권이 필요할 때 사용할 데코레이터

# def get(self, request, *args, **kwargs): 를 받으므로 인자들 그대로 가져오기
from django.contrib.auth.models import User
from django.http import HttpResponseForbidden


def account_ownership_required(func):
    def decorated(request, *args, **kwargs):
        # DB에서 직접 빼오기 = 사용자에서.어떤 객체를 뽑을 건지.단일 객체(고유값 설정 =키워드[고유값])
        target_user = User.objects.get(pk = kwargs['pk'])
        if target_user == request.user:
            return func(request, *args, **kwargs)
        else:
            # ()쓰면 호출
            return HttpResponseForbidden()
    return decorated

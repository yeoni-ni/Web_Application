from django.http import HttpResponseForbidden

from profileapp.models import Profile

# 프로필 소유권 여부 확인
def profile_ownership_required(func):
    def decorated(request, *args, **kwargs):
        # DB에서 프로필 가져오기
        target_profile = Profile.objects.get(pk = kwargs['pk'])
        if target_profile.user == request.user:
            return func(request, *args, **kwargs)
        else:
            return HttpResponseForbidden()
    return decorated

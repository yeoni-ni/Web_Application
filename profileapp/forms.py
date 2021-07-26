from django.forms import ModelForm

# 장고 구문 형태
from profileapp.models import Profile


class ProfileCreationForm(ModelForm):
    class Meta:
        model = Profile
        # 클라이언트한테 3가지 Data 받음
        fields = ['image','nickname','message']


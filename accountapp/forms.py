from django.contrib.auth.forms import UserCreationForm


class AccountCreationForm(UserCreationForm):
    # 초기화 메서드 작성
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # ID칸 비활성화
        self.fields['username'].disabled = True
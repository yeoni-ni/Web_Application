from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView

from profileapp.decorators import profile_ownership_required
from profileapp.forms import ProfileCreationForm
from profileapp.models import Profile

@method_decorator(login_required,'get')
@method_decorator(login_required,'post')
class ProfileCreateView(CreateView):
    model = Profile
    # 입력 받는 form
    form_class = ProfileCreationForm
    # success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'profileapp/create.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        # 부모 메소드 불러오기
        return super().form_valid(form)

    # self.object = target_profile 이라 생각
    def get_success_url(self):
        return reverse('accountapp:detail', kwargs={'pk': self.object.user.pk})

@method_decorator(profile_ownership_required, 'get')
@method_decorator(profile_ownership_required, 'post')
class ProfileUpdateView(UpdateView):
    model = Profile
    context_object_name = 'target_profile'
    form_class = ProfileCreationForm
    # success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'profileapp/update.html'

    # self.object = target_profile 이라 생각
    def get_success_url(self):
        return reverse('accountapp:detail', kwargs={'pk': self.object.user.pk})




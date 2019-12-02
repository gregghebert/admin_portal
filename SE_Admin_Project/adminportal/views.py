from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import UserInfo
from django.views.generic.base import TemplateView
from django.contrib.auth.models import User
from .forms import UserRegisterForm


class LinkPageView(TemplateView):
    template_name = 'adminportal/links.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        userprof = UserInfo.objects.filter(
            email=User.objects.get(email=self.request.user.email))
        profile_made = (len(userprof) != 0)
        context['profile_made'] = profile_made
        return context


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            fullName = form.cleaned_data.get('fullName')
            email = form.cleaned_data.get('email')
            messages.success(request, f'Account created for {fullName}!')
            return redirect("/")
    else:
        form = UserRegisterForm()
    return render(request, "adminportal/register.html", {'form': form})

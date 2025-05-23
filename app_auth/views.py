from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from app_auth.forms import RegisterForm


# Create your views here.

class RegisterView(View):
    form_class = RegisterForm
    template_name = 'app_auth/register.html'

    def get(self, request):
        return render(request, self.template_name, {"form": self.form_class})

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(to="/")
        return super().dispatch(request, *args, **kwargs)

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            messages.success(request, f"Вітаємо {username}. Ваш акаунт успішно створено")
            return redirect(to="app_auth:signin")
        return render(request, self.template_name, {"form": form})

class CustomLogoutView(View):
    template_name = 'app_auth/logout.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        logout(request)
        return redirect('app_auth:signin')
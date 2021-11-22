from django.shortcuts import render
from django.views import View


class IndexView(View):
    template_name = "sb_admin/index.html"

    def get(self, *args, **kwargs):
        return render(self.request, self.template_name)


class ButtonsView(View):
    template_name = "sb_admin/buttons.html"

    def get(self, *args, **kwargs):
        return render(self.request, self.template_name)


class CardsView(View):
    template_name = "sb_admin/cards.html"

    def get(self, *args, **kwargs):
        return render(self.request, self.template_name)


class Error404View(View):
    template_name = "sb_admin/404.html"

    def get(self, *args, **kwargs):
        return render(self.request, self.template_name)


class BlankView(View):
    template_name = "sb_admin/blank.html"

    def get(self, *args, **kwargs):
        return render(self.request, self.template_name)


class ChartsView(View):
    template_name = "sb_admin/charts.html"

    def get(self, *args, **kwargs):
        return render(self.request, self.template_name)


class ForgotPasswordView(View):
    template_name = "sb_admin/forgot-password.html"

    def get(self, *args, **kwargs):
        return render(self.request, self.template_name)


class LoginView(View):
    template_name = "sb_admin/login.html"

    def get(self, *args, **kwargs):
        return render(self.request, self.template_name)


class RegisterView(View):
    template_name = "sb_admin/register.html"

    def get(self, *args, **kwargs):
        return render(self.request, self.template_name)


class TablesView(View):
    template_name = "sb_admin/tables.html"

    def get(self, *args, **kwargs):
        return render(self.request, self.template_name)

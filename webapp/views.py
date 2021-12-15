from django.shortcuts import render
from django.views import View
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


class CustomizedAdminLoginView(View):
    def get(self, request):
        if request.user.is_authenticated:
            pass  # TODO later
        redirect_to = request.GET.get('next', '/')
        if redirect_to:
            pass

        defaults = {
            'extra_context': {},
            'template_name': 'admin/login.html',
        }
        return LoginView.as_view(**defaults)(request)

    def post(self, request):
        from django.contrib.admin.sites import AdminSite
        adminsite = AdminSite(name='admin')
        return adminsite.login(request, {})


def logout(request):
    auth_logout(request)
    return HttpResponseRedirect('/')


class UserProfileView(View):
    template_name = "default/webapp/userprofile.html"

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        return render(request, self.template_name, {"msg": ''})


class DashboardView(View):
    template_name = "default/webapp/dashboard.html"

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        return render(request, self.template_name, {"msg": ''})


class ListIndexView(View):
    template_name = "default/webapp/list_index.html"

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        return render(request, self.template_name, {})
from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.http import HttpResponseNotFound
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .forms import AddCatForm, RegisterUserForm, LoginUserForm
from .models import Cat
from .utils import CatManagerData, ContextMixin


class ShowCatList(ContextMixin, ListView):
    """ Представление страницы со всеми котами """
    model = Cat
    template_name = 'cats/cats.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        extra_context = self.get_context(title='Котики')
        result_context = dict(list(context.items()) + list(extra_context.items()))
        return result_context


class ShowCat(ContextMixin, DetailView):
    """ Представление страницы с котом """
    model = Cat
    template_name = 'cats/cat_id.html'
    slug_url_kwarg = 'cat_slug'
    context_object_name = 'cat'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        extra_context = self.get_context(title=self.object.name)
        result_context = dict(list(context.items()) + list(extra_context.items()))
        return result_context


class AddCat(ContextMixin, CreateView):
    """ Добавление кота """
    form_class = AddCatForm
    template_name = 'cats/add_cat.html'
    success_url = reverse_lazy('cats')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        extra_context = self.get_context(title='Добавление кота')
        result_context = dict(list(context.items()) + list(extra_context.items()))
        return result_context

    def form_valid(self, form):
        """ Автоматическое добавление параметров """
        CatManagerData().set_author(self, form)
        CatManagerData().set_slug(self, form)
        self.object.save()
        return redirect('cats')


class DeleteCat(ContextMixin, DeleteView):
    """ Удаление кота """
    model = Cat
    fields = ['name', 'age', 'breed', 'weight', 'photo', 'description']
    template_name = 'cats/del_cat.html'
    slug_url_kwarg = 'cat_slug'
    success_url = reverse_lazy('cats')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        extra_context = self.get_context(title='Удаление кота', slug=self.object.slug, name=self.object.name)
        result_context = dict(list(context.items()) + list(extra_context.items()))
        return result_context


class UpdateCat(ContextMixin, UpdateView):
    """ Редактирование кота """
    model = Cat
    fields = ['name', 'age', 'breed', 'weight', 'photo', 'description']
    template_name = 'cats/upd_cat.html'
    slug_url_kwarg = 'cat_slug'
    success_url = reverse_lazy('cats')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        extra_context = self.get_context(title='Редактирование кота', slug=self.object.slug)
        result_context = dict(list(context.items()) + list(extra_context.items()))
        return result_context


class RegisterUser(ContextMixin, CreateView):
    """ Регистрация пользователя """
    form_class = RegisterUserForm
    template_name = 'user/register.html'
    success_url = reverse_lazy('cats')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        extra_context = self.get_context(title='Регистрация')
        result_context = dict(list(context.items()) + list(extra_context.items()))
        return result_context

    def form_valid(self, form):
        """ Вход сразу после регистрации """
        user = form.save()
        login(self.request, user)
        return redirect('cats')


class LoginUser(ContextMixin, LoginView):
    """ Авторизация пользователя """
    form_class = LoginUserForm
    template_name = 'user/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        extra_context = self.get_context(title='Авторизация')
        result_context = dict(list(context.items()) + list(extra_context.items()))
        return result_context

    def get_success_url(self):
        return reverse_lazy('cats')


def logout_user(request):
    """ Выход пользователя """
    logout(request)
    return redirect('login')


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1> Страница не найдена <h1>")

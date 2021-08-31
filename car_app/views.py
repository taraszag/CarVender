from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# from django.contrib.auth.decorators import login_required
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .filter import SellFilter

from .models import *


# Create your views here.
def index(request):
    posts = Sellrequest.objects.all()
    return render(request, 'car_app/index.html', {"posts": posts})


# Views Sells detail
class SellDetailViews(DetailView):
    model = Sellrequest


# Sell list views and filter Sells
class FilterSellListView(ListView):
    filter_class = None

    def get_queryset(self):
        qs = super().get_queryset()
        req = self.request.GET
        self.filtered = self.filter_class(req, qs)
        return self.filtered.qs.distinct()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["filter"] = self.filtered
        return context


class SellListView(FilterSellListView):
    model = Sellrequest
    filter_class = SellFilter
    template_name = "car_app/index.html"
    context_object_name = "posts"
    paginate_by = 5


# user sells Views
class UserSellListView(ListView):
    model = Sellrequest
    template_name = "car_app/user_posts.html"
    context_object_name = "posts"
    paginate_by = 3

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get("username"))
        return Sellrequest.objects.filter(Author=user)


# CRUD Views Sells
class SellCreateView(LoginRequiredMixin, CreateView):
    model = Sellrequest
    fields = "__all__"

    def form_valid(self, form):
        form.instance.Author = self.request.user
        return super().form_valid(form)


class SellUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Sellrequest
    fields = "__all__"

    def form_valid(self, form):
        form.instance.Author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        sell = self.get_object()
        return self.request.user == sell.Author


class SellDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Sellrequest
    success_url = "/"

    def test_func(self):
        sell = self.get_object()
        return self.request.user == sell.Author


# return resto http requests

def about(request):
    return render(request, 'car_app/about.html')


def help_fq(request):
    return render(request, 'car_app/help.html')


def contacts(request):
    return render(request, 'car_app/about.html')


# return error's
def page_not_found(request, exception):
    context = None
    if "tried" in str(exception):

        context = {"exception": "Page not found"}
    else:
        context = {"exception": exception}
        print(exception)
    return render(request, 'car_app/404.html', context)

# def error403(request, exception):
#     context = {"exception": exception}
#     return render(request, 'car_app/403.html', context)
#
#
# def error500(request, exception):
#     context = {"exception": exception}
#     return render(request, 'car_app/500.html', context)

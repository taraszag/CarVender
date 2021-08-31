"""CarVender URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from car_app import views
from user import views as user_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # posts and home urls
    path('admin/', admin.site.urls),
    path('', views.SellListView.as_view(), name="car_app-home"),
    path('about/', views.about, name="car_app-about"),
    path('help/', views.help_fq, name="car_app-help"),
    path('contacts/', views.contacts, name="car_app-contacts"),
    path('sell/<int:pk>/', views.SellDetailViews.as_view(), name="car_app-detail"),
    path('profile/<int:pk>/', user_views.UserDetailViews.as_view(), name="profile-detail"),
    path('sell/new/', views.SellCreateView.as_view(), name="car_app-create"),
    path('sell/<int:pk>/update', views.SellUpdateView.as_view(), name="car_app-update"),
    path('sell/<int:pk>/delete', views.SellDeleteView.as_view(), name="car_app-delete"),
    path('sell/user/<str:username>', views.UserSellListView.as_view(), name="car_app-user_posts"),
    # users urls
    path('accounts/profile/', user_views.profile, name="user-profile"),
    path('register/', user_views.register, name="user-register"),
    path('login/', auth_views.LoginView.as_view(template_name="user/login.html"), name="user-login"),
    path('logout/', auth_views.LogoutView.as_view(template_name="user/logout.html"), name="user-logout"),
    # #cart urls
    # path('cart/', cart_views.cart_detail, name='cart_detail'),
    # path('add/<int:product_id>/', cart_views.cart_add, name='cart_add'),
    # path('remove/<int:product_id>/', cart_views.cart_remove, name='cart_remove'),
    # #path('success_register/', name="user-success_register"),\

    # path("password-reset/",
    #      auth_views.PasswordResetView.as_view(template_name="user/password_reset.html"),
    #      name="user-password_reset"),
    # path("password-reset/",
    #      auth_views.PasswordResetDoneView.as_view(template_name="user/password_reset_done.html"),
    #      name="user-password_reset_done"),
    # path("password-reset-confirm/<uidb64>/<token>",
    #      auth_views.PasswordResetConfirmView.as_view(template_name="user/password_reset_confirm.html"),
    #      name="password_reset_confirm"),

]

handler404 = 'car_app.views.page_not_found'
# handler500 = 'car_app.views.error500'
# handler403 = 'car_app.views.error403'

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

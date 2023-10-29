from django.urls import path

from django.contrib.auth import views as auth_views

from . import views


urlpatterns = [
    path('register/', views.Register, name="register"),
    path('login/', views.Login, name="login"),
    path('logout/', views.LogoutUser, name="logout"),

    path('', views.home, name="home"),
    path('user/', views.UserPage, name="user"),
    path('account/', views.AccountSettings, name="account"),

    path('products/', views.products, name="products"),
    path('customer/<str:pk>/', views.customer, name="customer"),

    path('create_order/<str:pk>/', views.CreateOrder, name="create_order"),
    path('update_order/<str:pk>/', views.UpdateOrder, name="update_order"),
    path('delete_order/<str:pk>/', views.DeleteOrder, name="delete_order"),


  # https://docs.djangoproject.com/en/4.2/topics/auth/default/#all-authentication-views
  # https://github.com/django/django/blob/main/django/contrib/auth/views.py

    path("password_reset/", auth_views.PasswordResetView.as_view(template_name="accounts/password_reset.html"), name="password_reset"),
    path(
        "password_reset/done/",
        auth_views.PasswordResetDoneView.as_view(template_name="accounts/password_reset_sent.html"),
        name="password_reset_done",
    ),
    path(
        "reset/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(template_name="accounts/password_reset_form.html"),
        name="password_reset_confirm",
    ),
    path(
        "reset/done/",
        auth_views.PasswordResetCompleteView.as_view(template_name="accounts/password_reset_done.html"),
        name="password_reset_complete",
    ),

    
]

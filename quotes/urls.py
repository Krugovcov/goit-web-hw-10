from django.urls import path, include
from django.contrib.auth import views as auth_views

from . import views

app_name = "quotes"
urlpatterns = [
    path('', views.index, name='home'),  # app_photo:home
    path('add/quote/', views.add_quote, name='add_quote'),
    path('add/author/', views.add_author, name='add_author'),
    path('add/tag/', views.add_tag, name='add_tag'),
    path('author/<int:author_id>/', views.author_detail, name='author_detail'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]

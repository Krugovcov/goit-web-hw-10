from django.urls import path, include

from . import views

app_name = "quotes"
urlpatterns = [
    path('', views.index, name='home'),  # app_photo:home
    path('add/quote/', views.add_quote, name='add_quote'),
    path('add/author/', views.add_author, name='add_author'),
    path('add/tag/', views.add_tag, name='add_tag'),
    path('author/<int:author_id>/', views.author_detail, name='author_detail'),
]

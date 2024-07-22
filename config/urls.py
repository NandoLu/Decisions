from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("app.urls")),
    path('login/', LoginView.as_view(), name="login"),
    # path('livros/', LivrosView.as_view(), name='livros'),
    # path('reserva/', EmprestimoView.as_view(),name='reserva'),
    # path('cidade/', CidadeView.as_view(),name='cidade'),
    # path('autor/', AutoresView.as_view(), name='autor'),
    # path('editor/', EditorasView.as_view(),name='editora'),
    # path('leitor/', UsuarioView.as_view(),name='leitor'),
    # path('genero/', GenerosView.as_view(),name='genero'),
]
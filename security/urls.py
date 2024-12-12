from django.urls import path
from . import views
urlpatterns = [
    path('login/', views.connexion),
    path('signup/', views.inscription),
    path('test/', views.TestView),
    path('refresh/', views.refreshToken),
    path('profil/', views.profilUser),
    path('logout/', views.deconnexion)
]
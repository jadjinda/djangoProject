from django.urls import path
from . import views
urlpatterns = [
    path('add-budget/', views.create),
    path('get-budget/', views.list),
    path('getOne-budget/<int:id>/', views.get_one),
    path('update-budget/<int:id>/', views.update),
    path('delete-budget/<int:id>/', views.delete)
]
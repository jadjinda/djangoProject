from django.urls import path
from . import views
urlpatterns = [
    path('add-dette/', views.create),
    path('get-dette/', views.list),
    path('getOne-dette/<int:id>/', views.get_one),
    path('update-dette/<int:id>/', views.update),
    path('delete-dette/<int:id>/', views.delete)
]
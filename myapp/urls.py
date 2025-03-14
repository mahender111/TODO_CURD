from django.urls import path
from . import views
# from .views import TodoList

urlpatterns = [
    path('home/',views.index, name="index_url")
    # path('TodoList/', TodoList.as_view(), name='TodoList'),
]
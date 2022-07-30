from django.urls import path
from .views import DetailTodo, ListTodo

app_name = "api"

urlpatterns = [
    path("<int:pk>/", DetailTodo.as_view(), name="detail_todo"),
    path("", ListTodo.as_view(), name="list_todo"),
]

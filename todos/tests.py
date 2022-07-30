from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse

from todos.serializers import TodoSerializer

from .models import Todo

class TestTodo(APITestCase):
    def setUp(self):
        self.todo = Todo.objects.create(
            title="todo title",
            body="todo body",
        )

    def test_model_content(self):
        self.assertEqual(self.todo.title, "todo title")
        self.assertEqual(self.todo.body, "todo body")
        self.assertEqual(str(self.todo), "todo title")

    def test_todo_listview(self):
        response = self.client.get(reverse("api:list_todo"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Todo.objects.count(), 1)
        self.assertContains(response, self.todo)

    def test_todo_detailview(self):
        url = reverse("api:detail_todo", kwargs={"pk":1})
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Todo.objects.count(), 1)
        self.assertContains(response, self.todo)

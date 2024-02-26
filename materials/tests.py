from rest_framework import status
from rest_framework.test import APITestCase

from materials.models import Lesson


class LessonTestCase(APITestCase):
    def setUp(self) -> None:
        self.data = {
            'name': 'test',
            'description': 'test'
        }

    def test_create_lesson(self):
        """Тестирование создания урока"""

        response = self.client.post(
            '/lesson/',
            data=self.data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )
    #
    #     self.assertEqual(
    #         response.json(),
    #         {}
    #     )
    #     self.assertTrue(
    #         Lesson.objects.all().exists
    #     )
    #
    # def test_lesson_list(self):
    #     """Тестирование вывода списка уроков"""
    #
    #     response = self.client.get(
    #         '/lesson/'
    #     )
    #     self.assertEqual(
    #         response.status_code,
    #         status.HTTP_200_OK
    #     )
    #     self.assertEqual(
    #         response.json(),
    #         [{}]
    #     )

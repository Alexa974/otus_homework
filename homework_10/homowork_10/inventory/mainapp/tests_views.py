from django.test import TestCase
from .models import Device, User, Card

class TestViews(TestCase):

    def test_status_code(self):
        response = self.client.get('/')
        # response_1 = self.client.get('/device-list/')
        self.assertEquals(response.status_code, 200)
        # self.assertEquals(response_1.status_code, 200)

    def test_status_code_1(self):
        response = self.client.get('/device-list/')
        # response_1 = self.client.get('/device-list/')
        self.assertEquals(response.status_code, 200)
        # self.assertEquals(response_1.status_code, 200)

    def test_context(self):
        card = Card.objects.create(title='Карточка № 1')

        response = self.client.get('/')
        # print(response.context)
        self.assertTrue('cards' in response.context)

    def test_content(self):
        response = self.client.get('/')
        button_element = '<button class="btn btn-outline-success" type="submit">Search</button>'

        self.assertIn(button_element, response.content.decode(encoding='utf-8'))

        # print(response.content)
        # print(type(response.content))



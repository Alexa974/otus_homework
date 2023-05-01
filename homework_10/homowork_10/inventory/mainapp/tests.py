from django.test import TestCase
from .models import Device, User, Card

class TestDevice(TestCase):

    def setUp(self):
        self.device = Device.objects.create(type='device_type_1')
        print('Выполнение перед каждым тестом')

    def tearDown(self):
        print('Выполнение после каждого теста тестом')

    def test_init(self):
        self.assertEquals(self.device.type, 'device_type_1')

    def test_str(self):
        self.assertEquals(str(self.device), 'device_type_1')

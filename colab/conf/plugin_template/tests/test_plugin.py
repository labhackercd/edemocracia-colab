
from django.test import TestCase, Client


class {{ app_name_camel }}PluginTest(TestCase):

    def setUp(self):
        self.client = Client()

    def test_true(self):
        assert True

from django.test import TestCase
from django.utils.six import assertRegex

class TestIfChanged(TestCase):
    def test_if_changed(self):
        resp = self.client.get('/')
        assertRegex(self, resp.content, '1\s+2\s+3')

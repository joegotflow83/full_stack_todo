from django.core.urlresolvers import reverse
from rest_framework.test import APITestCase


class APITest(APITestCase):
    """API Test Cases"""
    def test_get_all_tasks(self):
        resp = self.client.get(reverse('lc_all_tasks'))
        self.assertTrue(resp.status_code, 200)

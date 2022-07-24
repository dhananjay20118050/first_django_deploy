from django.test.testcases import SimpleTestCase
from django.urls.base import resolve


class APIUrlsTest(SimpleTestCase):
    def test_get_customers_is_resolved(self):
        url = resolve('Customer')
        print(url)
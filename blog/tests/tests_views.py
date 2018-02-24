from django.test import TestCase
from blog.blog_views import searchlist
from django.test.client import Client



class SearchListTest(TestCase):
    c = Client()

    def test_search_query(self):
        resp = self.c.get('/?search_box=immigration')
        self.assertEqual(resp.status_code, 200)

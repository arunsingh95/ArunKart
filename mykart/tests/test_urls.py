from django.test import SimpleTestCase
from django.urls import reverse, resolve
from mykart.urls import *
from mykart.views import *


class TestUrls(SimpleTestCase):

    def test_login_url(self):
        test_url = reverse('login')
        match_url = resolve(test_url)
        print(resolve(test_url))
        self.assertEquals(match_url.func.view_class, LoginView)

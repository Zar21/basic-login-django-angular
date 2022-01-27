from django.test import TestCase, Client
from django.contrib.auth import get_user_model


class TestUser(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user('test@test.com', 'test/test')

    def test_not_authenticated(self):
        client = Client()

        response = client.get('/api/user')
        self.assertEquals(response.status_code, 403)

    def test_authenticated(self):
        client = Client()
        response = client.post('/api/login', {
            "email": "test@test.com",
            "password": "test/test"
        }, content_type='application/json')
        self.assertEquals(response.status_code, 200)
        self.assertTrue(response.data["token"])
        response = client.get('/api/user',
                              **{'HTTP_AUTHORIZATION': f'Bearer {response.data["token"]}'})
        self.assertEquals(response.status_code, 200)

    def test_update_user(self):
        client = Client()
        response = client.post('/api/login', {
            "email": "test@test.com",
            "password": "test/test"
        }, content_type='application/json')
        response = client.put('/api/user', {"first_name": "TEST"},
                              content_type='application/json',
                              ** {'HTTP_AUTHORIZATION': f'Bearer {response.data["token"]}'})
        self.assertEquals(response.data["first_name"], "TEST")

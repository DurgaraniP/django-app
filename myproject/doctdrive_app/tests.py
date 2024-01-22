from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import CustomUser

class CustomUserTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user_data = {'username': 'badri', 'email': 'badri@gamil.com', 'password': '123456789'}
        self.user = CustomUser.objects.create_user(**self.user_data)
        self.login_url = reverse('signin')

    def test_create_user(self):
        response = self.client.post(reverse('signup'), self.user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(CustomUser.objects.count(), 2)  # Change to 1 if not using a persistent database

    def test_user_login(self):
        response = self.client.post(self.login_url, {'email': 'test@example.com', 'password': 'testpassword'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, 'token')

    def test_user_details_view(self):
        url = reverse('user-details', args=[self.user.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, 'testuser')

    def tearDown(self):
        pass

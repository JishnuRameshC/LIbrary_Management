from django.test import TestCase
from django.contrib.auth import get_user_model

from .forms import CustomUserChangeForm,CustomUserCreationForm
# Create your tests here.

class CustomUserTest(TestCase):
    def setUp(self):
        pass

    def test_create_user(self):
        User =get_user_model()
        user=User.objects.create_user(
            email='testuser1@gmail.com',
            username= 'testuser1',
            password= 'testpass123'
        )
        self.assertEqual(user.email,'testuser1@gmail.com')
        self.assertEqual(user.username,'testuser1')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        user = User.objects.create_superuser(
            email = 'testuser2@gmail.com',
            username = 'testuser2',
            password = 'testpass123',
        )
        self.assertEqual(user.email,'testuser2@gmail.com')
        self.assertEqual(user.username,'testuser2')
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)
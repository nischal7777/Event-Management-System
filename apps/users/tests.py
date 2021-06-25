from django.test import TestCase
from django.contrib.auth import get_user_model
import traceback
# Create your tests here.

# AbstractUser => Use if you want to change a particular field from default user model.

# AbstractBaseUser => Use if you want to build custom user model from scratch.

class UserManagersTest(TestCase):

    def test_create_user(self):
        Users = get_user_model()
        user = Users.objects.create_user(email="user@gmail.com", password="user")
        self.assertEqual(user.email, 'user@gmail.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        try:
            # username is None for AbstractUser
            # username field doesn't exists for AbstractBaseUser
            self.assertIsNone(user.username)
        except AttributeError:
            pass
        with self.assertRaises(TypeError):
            Users.objects.create_user()
        with self.assertRaises(TypeError):
            Users.objects.create_user(email="")
        with self.assertRaises(ValueError):
            Users.objects.create_user(email="",password="user")

    def test_create_superuser(self):
        Users = get_user_model()
        user = Users.objects.create_superuser(email="admin@gmail.com", password="admin")
        self.assertEqual(user.email, 'admin@gmail.com')
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)
        try:
            # username is None for AbstractUser
            # username field doesn't exists for AbstractBaseUser
            self.assertIsNone(user.username)
        except AttributeError:
            pass

        with self.assertRaises(ValueError):
            Users.objects.create_superuser(email="admin@gmail.com", password="admin", is_superuser=False)

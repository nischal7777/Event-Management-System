from django.contrib.auth.base_user import BaseUserManager

class CustomUserManager(BaseUserManager):
    """
    custom user model manager where email is the unique identifier rather
    than username
    """
    def create_user(self, email, password, **kwargs):
        """
        Creating a user with provided email and password
        """
        if not email:
            raise ValueError("Email must be provided.")
        email = self.normalize_email(email=email)
        user = self.model(email=email, **kwargs)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **kwargs):
        """
        Creating a super user with provided email and password
        """
        kwargs.setdefault('is_staff', True)
        kwargs.setdefault('is_superuser', True)
        kwargs.setdefault('is_active', True)
        

        if kwargs.get('is_staff') is not True:
            raise ValueError("super user must be a staff (is_staff=True).")
        
        if kwargs.get('is_superuser') is not True:
            raise ValueError("super user must have is_superuser=True.")

        return self.create_user(email, password, **kwargs)

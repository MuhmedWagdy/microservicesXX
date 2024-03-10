from django.db import models
from django.contrib.auth.models import AbstractUser,AbstractBaseUser,BaseUserManager



class CustomUserManager(BaseUserManager):
    def create_user(self,email,password=None,**extra_fields):
        if not email :
            raise ValueError('The email feild is Required')
        
        email = self.normalize_email(email)
        user = self.model(email=email,**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self,email,password=None,**extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        return self.create_user(email,password,**extra_fields)
    








class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=25,null=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    
    objects = CustomUserManager()


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []     # login 

    def __str__(self):
        return self.email






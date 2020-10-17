from django.db import models
from django.contrib.auth.models import AbstractBaseUser , BaseUserManager

# Create your models here.

# Custom User Model Manager 
class UserModelManager(BaseUserManager):
    def create_user(self,email,password=None,username=None):
        if not email:
            return ValueError('Email is a Mandatory Field')
        
        user = self.model(
            email = self.normalize_email(email),
            
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,email,password=None,username=None):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password

        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user    


# Custom User Model
class UserModel(AbstractBaseUser):
    email = models.CharField(
        unique=True,
        verbose_name='Email Address',
        max_length=50
        )
    date_joined = models.DateField(auto_now=True)
    last_login = models.DateField(auto_now_add=True)
    username = models.CharField(null=True,max_length=10)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    

    USERNAME_FIELD='email'
    REQUIRED_FIELDS = []

    objects = UserModelManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    



from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

from django.db import models

class UserManager(BaseUserManager):
    """ User Model Manager """

    def create_user(self, username, password, is_staff=False, is_admin=False, is_active=True):
        if not username:
            raise ValueError('Users must have username')
        if not password:
            raise ValueError('User must have Password')
        # if not full_name:
        #     raise ValueError('User must have a full name')
        user_obj = self.model()
        user_obj.set_password(password)
        user_obj.is_staff = is_staff
        user_obj.is_admin = is_admin
        user_obj.is_active = is_active
        user_obj.save(using=self._db)



    def create_superuser(self, username, password):
        user = self.create_user(
            username,
            password=password,
            is_staff=True,
            is_admin=True
        )
        return user



class User(AbstractBaseUser):
    """
    Custom abstract user Model.
    """

    # Names

    username = models.CharField(max_length=30, blank=False, null=False)
    password = models.CharField(max_length=30, blank=False, null=False)
    # this is not the best way to create a  phone number
    phone_number = models.CharField(max_length=15, blank=False, null=False,unique=True)
   #___________________________________________________________________________________
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # Permission
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    # Main Field for authentication
    USERNAME_FIELD = 'phone_number'

    # When user create must need to fill this field
    REQUIRED_FIELDS = ["username","password"]

    objects = UserManager()

    def __str__(self):
        return self.username

    class Meta:
        ordering = ('-created_at', '-updated_at', )



    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
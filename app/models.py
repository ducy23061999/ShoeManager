from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser

# Create your models here.
# ------------- Role-------------------
class Role(models.Model):
    role = models.CharField(max_length=50)
# ------------- User-------------------
class CustomUserManager(BaseUserManager):

    def create_user(self, username, first_name, last_name, password=None):
        if not username:
            raise ValueError("User must have an email")
        if not password:
            raise ValueError("User must have a password")
        if not first_name:
            raise ValueError("User must have a first name")
        if not last_name:
            raise ValueError("User must have a last name")

        user = self.model(
            username=username
        )
        user.first_name = first_name
        user.last_name = last_name
        user.set_password(password)  # change password to hash

        role = Role.objects.get(pk=1)
        user.role = role
        user.is_admin = False
        user.is_staff = False
        user.save(using=self._db)
        return user

    def create_superuser(self, username, first_name, last_name, password=None):
        if not username:
            raise ValueError("User must have an email")
        if not password:
            raise ValueError("User must have a password")
        if not first_name:
            raise ValueError("User must have a first name")
        if not last_name:
            raise ValueError("User must have a last name")

        user = self.model(
            username=username
        )
        user.first_name = first_name
        user.last_name = last_name
        user.set_password(password)  # change password to hash

        role = Role.objects.get(roleId=2)
        user.role = role

        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    username = models.CharField(max_length=200, unique=True)
    first_name = models.CharField(max_length=30, default='')
    last_name = models.CharField(max_length=30, default='')

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)  # a admin user; non super-user
    is_admin = models.BooleanField(default=False)

    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    address = models.CharField(max_length=500)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = CustomUserManager()

    @staticmethod
    def has_perm(perm, obj=None):
        # "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    @staticmethod
    def has_module_perms(app_label):
        return True

    def __str__(self):
        return "{}".format(self.username)



# ------------- SIZE -----------------

class Size(models.Model):
    size = models.IntegerField()
# ------------- Shoe--------------------

class Shoe(models.Model):
    name = models.CharField(max_length=200)
    manufactor = models.CharField(max_length=500)
    image = models.CharField(max_length=2000, default="")
    price = models.IntegerField()


# ------------- Shoe--------------------

class Stock(models.Model):
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    shoe = models.ForeignKey(Shoe, on_delete=models.CASCADE)
    amount = models.IntegerField(default=0)
    class Meta:
        unique_together = (("size", "shoe"))
#--------------Promotion----------------------

class Promotion(models.Model):
    name = models.CharField(max_length=200, default="")
    promote = models.FloatField()
    is_used = models.BooleanField(default=False)

#--------------Cart----------------------

class Cart(models.Model):
    user_create = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True, blank=True)
    promote = models.ForeignKey(Promotion, on_delete=models.CASCADE, blank=True, null=True)
    da_duyet = models.BooleanField(default=False)

# --------------CartDetail--------------------

class CartDetail(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    shoe = models.ForeignKey(Shoe, on_delete=models.CASCADE)
    amount = models.IntegerField()

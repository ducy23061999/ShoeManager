from django.db import models

# Create your models here.
# ------------- Role-------------------
class Role(models.Model):
    role = models.CharField(max_length=50)
# ------------- User-------------------
class User(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    address = models.CharField(max_length=500)
# ------------- SIZE -----------------
class Size(models.Model):
    size = models.IntegerField()

# ------------- Shoe--------------------
class Shoe(models.Model):
    name = models.CharField(max_length=200)
    manufactor = models.CharField(max_length=500)
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
    date = models.DateField()
    promote = models.ForeignKey(Promotion, on_delete=models.CASCADE)
# --------------CartDetail--------------------
class CartDetail(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    shoe = models.ForeignKey(Shoe, on_delete=models.CASCADE)
    amount = models.IntegerField()

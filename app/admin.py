from django.contrib import admin

# Register your models here.
from app.models import Role
from app.models import User
from app.models import Size
from app.models import Shoe
from app.models import Stock
from app.models import Promotion
from app.models import Cart
from app.models import CartDetail

admin.site.register(Role)
admin.site.register(User)
admin.site.register(Size)
admin.site.register(Shoe)
admin.site.register(Stock)
admin.site.register(Promotion)
admin.site.register(Cart)
admin.site.register(CartDetail)

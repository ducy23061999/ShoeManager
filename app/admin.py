from django.contrib import admin

# Register your models here.
from .models import Role
from .models import User
from .models import Size
from .models import Shoe
from .models import Stock
from .models import Promotion
from .models import Cart
from .models import CartDetail

admin.site.register(Role)
admin.site.register(User)
admin.site.register(Size)
admin.site.register(Shoe)
admin.site.register(Stock)
admin.site.register(Promotion)
admin.site.register(Cart)
admin.site.register(CartDetail)

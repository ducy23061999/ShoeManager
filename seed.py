from app.models import Role, User, CartDetail, Cart, Shoe, Size, Promotion, Stock
from django_seed import Seed

seeder = Seed.seeder()

seeder.add_entity(Role, 1, {
    'role': 'user'
})

seeder.add_entity(Role, 2, {
    'role': 'admin'
})
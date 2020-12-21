from app.models import Role
from django_seed import Seed

seeder = Seed.seeder()

seeder.add_entity(Role, 1, {
    'role': 'user'
})

seeder.add_entity(Role, 2, {
    'role': 'admin'
})
from django.core.management.base import BaseCommand

from user_app.models import User

users = [
    {
        'username': 'user1',
        'first_name': 'Frodo',
        'last_name': 'Baggins',
        'email': 'frodo@localhost'
    },
    {
        'username': 'user2',
        'first_name': 'Samwise',
        'last_name': 'Gamgee',
        'email': 'samwise@localhost'
    },
    {
        'username': 'user3',
        'first_name': 'Peregrin',
        'last_name': 'Took',
        'email': 'peregrin@localhost'
    },
    {
        'username': 'user4',
        'first_name': 'Meriadoc',
        'last_name': 'Brandybuck',
        'email': 'meriadoc@localhost'
    }]


class Command(BaseCommand):
    def handle(self, *args, **options):
        User.objects.create_superuser('admin', 'admin@localhost', 'admin')

        for user in users:
            new_user = User(**user)
            new_user.save()


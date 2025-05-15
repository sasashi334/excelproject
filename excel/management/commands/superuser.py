from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.conf import settings

User = get_user_model

class Command(BaseCommand):
    def handle(self, *args, **option):
        if not User.objects.filter(username='sasashi334').exists():
            User.objects.create_superuser(
                username='sasashi334',
                email='',
                password='sasashi334'
            )

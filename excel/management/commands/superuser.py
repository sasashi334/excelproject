from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.conf import settings
import os

User = get_user_model()


class Command(BaseCommand):
    def handle(self, *args, **option):
        superuser_name = os.environ.get("SUPERUSER_NAME")
        superuser_pass = os.environ.get("SUPERUSER_PASS")

        if not superuser_name or not superuser_pass:
            self.stdout.write("Environment variables SUPERUSER_NAME or SUPERUSER_PASS are missing. Skipping superuser creation.")
            return

        if not User.objects.filter(username=superuser_name).exists():
            User.objects.create_superuser(
                username=superuser_name,
                email="",
                password=superuser_pass,
            )
            self.stdout.write(f"Superuser '{superuser_name}' created.")

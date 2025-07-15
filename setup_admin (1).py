from django.contrib.auth import get_user_model
from django.core.management import BaseCommand
from django.db import IntegrityError

class Command(BaseCommand):
    help = "Create default superuser"

    def handle(self, *args, **options):
        User = get_user_model()
        username = "admin"
        email = "admin@example.com"
        password = "admin123"

        if not User.objects.filter(username=username).exists():
            try:
                User.objects.create_superuser(username=username, email=email, password=password)
                self.stdout.write(self.style.SUCCESS(f"Superuser '{username}' created successfully."))
            except IntegrityError:
                self.stdout.write(self.style.WARNING(f"User '{username}' already exists."))
        else:
            self.stdout.write(self.style.WARNING(f"Superuser '{username}' already exists."))

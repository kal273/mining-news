import os
import django
import logging

logging.basicConfig(level=logging.INFO)
print("Setting up Django...")

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from django.contrib.auth.models import User

if not User.objects.filter(username='admin').exists():
    print("Creating superuser 'admin'...")
    User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
    print("Superuser created successfully.")
else:
    print("Superuser 'admin' already exists.")

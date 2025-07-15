from django.contrib.auth import get_user_model
from django.db import IntegrityError

User = get_user_model()

username = "admin"
email = "admin@example.com"
password = "admin123"

if not User.objects.filter(username=username).exists():
    try:
        User.objects.create_superuser(username=username, email=email, password=password)
        print(f"Superuser '{username}' created successfully.")
    except IntegrityError:
        print(f"User '{username}' already exists.")
else:
    print(f"Superuser '{username}' already exists.")

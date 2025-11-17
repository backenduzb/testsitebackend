from django.apps import AppConfig
from django.db.utils import OperationalError

class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'

    def ready(self):
        from django.contrib.auth import get_user_model
        from django.db.models.signals import post_migrate

        def create_default_admin(sender, **kwargs):
            User = get_user_model()
            try:
                if not User.objects.filter(username="admin").exists():
                    User.objects.create_superuser(
                        username="admin",
                        password="admin123",
                        full_name="Default Admin"
                    )
                    print("✅ Default superuser yaratildi: admin / admin123")
            except OperationalError:
                pass

        post_migrate.connect(create_default_admin, sender=self)

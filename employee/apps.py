from django.apps import AppConfig


class EmployeeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'employee'
    verbose_name = "отдел кадров"
    verbose_name_plural = "отдел кадров"

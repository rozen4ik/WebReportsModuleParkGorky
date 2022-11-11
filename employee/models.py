from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Position(models.Model):
    name = models.CharField(max_length=150, verbose_name="уровень доступа")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "уровень доступа"
        verbose_name_plural = "уровни доступа"


# Таблица профиля связа с таблицей User
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="сотрудник")
    position_id = models.ForeignKey(Position, default=1, on_delete=models.CASCADE, verbose_name="уровень доступа")

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"

    class Meta:
        verbose_name = "профиль"
        verbose_name_plural = "профили"


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

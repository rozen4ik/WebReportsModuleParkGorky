from django.db import models


class Conf(models.Model):
    ip_kontur = models.CharField(max_length=250, verbose_name="ip контура")
    port_kontur = models.CharField(max_length=100, verbose_name="порт контура")
    path_to_db_kontur = models.CharField(max_length=300, verbose_name="путь к бд или алиас контура")
    user_db_kontur = models.CharField(max_length=250, verbose_name="логин для доступа к контуру")
    password_db_kontur = models.CharField(max_length=250, verbose_name="пароль для доступа к контуру")
    ip_ssh = models.CharField(max_length=250, verbose_name="ip для доступа по ssh к балону")
    user_ssh = models.CharField(max_length=250, verbose_name="логин для доступа по ssh к балону")
    password_ssh = models.CharField(max_length=250, verbose_name="пароль для доступа по ssh к балону")
    user_db_baloon = models.CharField(max_length=250, verbose_name="логин для доступа к бд балона")
    password_db_baloon = models.CharField(max_length=250, verbose_name="пароль для доступа к бд балона")

    class Meta:
        verbose_name = "настройки доступа"
        verbose_name_plural = "настройки доступа"


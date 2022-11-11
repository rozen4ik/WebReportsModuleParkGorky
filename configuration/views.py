from django.http import HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from configuration.models import Conf


def edit(request, id):
    try:
        config = Conf.objects.get(pk=1)

        data = {
            "config": config,
        }

        if request.method == "POST":
            config.ip_kontur = request.POST.get("ip_kontur")
            config.port_kontur = request.POST.get("port_kontur")
            config.path_to_db_kontur = request.POST.get("path_to_db_kontur")
            config.user_db_kontur = request.POST.get("user_db_kontur")
            config.password_db_kontur = request.POST.get("password_db_kontur")
            config.ip_ssh = request.POST.get("ip_ssh")
            config.user_ssh = request.POST.get("user_ssh")
            config.password_ssh = request.POST.get("password_ssh")
            config.user_db_baloon = request.POST.get("user_db_baloon")
            config.password_db_baloon = request.POST.get("password_db_baloon")
            config.save()
            return HttpResponseRedirect("/")
        else:
            return render(request, "conf/edit.html", data)

    except Conf.DoesNotExist:
        return HttpResponseNotFound("<h2>Страница не найдена</h2>")

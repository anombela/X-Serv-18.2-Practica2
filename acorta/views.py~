from django.shortcuts import render
from django.http import (HttpResponse,
                         HttpResponseNotFound, HttpResponseRedirect)
from models import Url
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


def printurls():

    urls = ""
    for url in Url.objects.all():
        urls += ("URL original: " + "<a href=" + url.url + ">" + url.url
                 + "</a>" + " --- URL acortada: " + "<a href="
                 + str(url.id) + ">" + "127.0.0.1:8000" + "/"
                 + str(url.id) + "</a><br>")
    return urls


@csrf_exempt
def urlacorta(request, recurso):

    formulario = ('<form action="" method="POST">Escribir url larga:'
                  + '<input type="text" name="nombre" value="" />'
                  + '<input type="submit" value="Acortar" /></form>')

    if request.method == 'POST':
        cuerpo = request.body.split('=')[1]
        if cuerpo == "":
            return HttpResponseNotFound(formulario + "Url no introducida")

        if cuerpo.find("http%3A%2F%2F") >= 0:
            cuerpo = cuerpo.split('http%3A%2F%2F')[1]

        cuerpo = "http://" + cuerpo
        try:
            newurl = Pages.objects.get(url=cuerpo)

        except:
            newurl = Url(url=cuerpo)
            newurl.save()

        return HttpResponse("URL original: " +
                            "<a href=" + cuerpo + ">" + cuerpo + "</a>" +
                            "</br>URL acortada: " +
                            "<a href=" + str(newurl.id) + ">" +
                            "127.0.0.1:8000" + "/" + str(newurl.id) + "</a>" +
                            "</p><a href=" + "http://127.0.0.1:8000" +
                            "> volver </a>""")

    if request.method == 'GET':
        urlList = Url.objects.all()
        if recurso == '':
            return HttpResponse(formulario + "Urls almacenadas:</br>"
                                + printurls())

        else:
            try:
                url = Url.objects.get(id=recurso)
                return HttpResponseRedirect(url.url)

            except:
                return HttpResponseNotFound("<h1>Pagina no encontrada</h1></p>"
                                            + "<a href=" + "http://" +
                                            "127.0.0.1:8000" + ">volver</a>")
    else:
        return ("<h1>404 Not Found</h1></p><a href=" + "http://127.0.0.1:8000"
                + "> volver </a>")

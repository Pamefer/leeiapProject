from django.shortcuts import render
#from .models import Facial
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import AnonymousUser
from django.views import View
import subprocess
import os, shutil
from mysite.settings import ALIGNED, RECOGNICE
import procesamiento

import time

import forms
from django.shortcuts import render, redirect
from mysite.settings import MEDIA_ROOT
from paieelApp.models import NumReconocimiento

def post_list(request):
    posts = "a"
    print(posts)
    return render(request, 'paieelApp/dashboard.html', {'post': posts})

def reconocimiento(request):
    return render(request, 'paieelApp/reconocimiento.html', {})

def send_command(request):

    #remove

    for the_file in os.listdir(ALIGNED):
        file_path = os.path.join(ALIGNED, the_file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print(e)
    #----

    commando = ["./util/align-dlib.py", "./training-images/", "align", "outerEyesAndNose", "./aligned-images/",
                    "--size", "96"]
    proc = subprocess.Popen(commando, cwd="/home/pamela/Escritorio/openface", stdout=subprocess.PIPE)
    out = proc.communicate()
    print out[0]

    # status = proc.returncode
    # print (status)
    # if status:
    #     # something went wrong
    #     print("not OK")
    #     pass
    # else:
    #     # we are ok
    #     print("OK")
    #     out = proc.communicate()
    #     print out[0]
    #     pass


    commando2 = ["./batch-represent/main.lua", "-outDir", "./generated-embeddings/", "-data", "./aligned-images/"]
    proc2 = subprocess.Popen(commando2, cwd="/home/pamela/Escritorio/openface", stdout=subprocess.PIPE)
    out2 = proc2.communicate()
    print out2[0]

    commando3 = ["./demos/classifier.py", "train", "./generated-embeddings/"]
    proc3 = subprocess.Popen(commando3, cwd="/home/pamela/Escritorio/openface", stdout=subprocess.PIPE)
    out3 = proc3.communicate()
    print out3[0]

    return render(request, 'paieelApp/reconocimiento.html', {})

class SubirFotoView(View):

    form_class = forms.IngresoForm
    template = 'paieelApp/reconocimiento.html'

    def render_form(self, request, form):
        return render(request, self.template, context={'form': form})

    def get(self, request):
        form = self.form_class()
        return self.render_form(request, form)

    def post(self, request):
        print(request)
        print(request.POST)
        print(request.FILES)
        print(request.FILES.get('foto'))
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            foto = request.FILES['foto']
            numero_reconocimientos = NumReconocimiento.objects.get_or_create(id=1)[0]
            foto_ruta = MEDIA_ROOT + "/%05d_" % numero_reconocimientos.num_reconocimientos + foto.name
            numero_reconocimientos.num_reconocimientos += 1
            numero_reconocimientos.save()
            with open(foto_ruta, "wb") as foto_file:
                for chunk in foto.chunks():
                    foto_file.write(chunk)
            usuario = request.user.pk
            if usuario == AnonymousUser:
                usuario = None
            procesamiento.ThreadingExample(foto=foto_ruta, fecha_hora=time.time(), user_logeado=usuario)
            return redirect('reconocer')
        else:
            return self.render_form(request, form)



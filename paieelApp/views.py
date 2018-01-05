from django.shortcuts import render
from .models import Facial
from django.shortcuts import render, get_object_or_404
import subprocess

def post_list(request):
    posts = Facial.objects.all()
    print(posts)
    return render(request, 'paieelApp/dashboard.html', {'post': posts})

def reconocimiento(request):
    if request.GET.get('entrenar'):
        commando = ["./util/align-dlib.py", "./training-images/", "align", "outerEyesAndNose", "./aligned-images/",
                        "--size", "96"]
        proc = subprocess.Popen(commando, cwd="/home/pamela/Escritorio/openface", stdout=subprocess.PIPE)
        out = proc.communicate()
        print out[0]
        return render(request, 'paieelApp/reconocimiento.html', {})
    else:
        return render(request, 'paieelApp/reconocimiento.html', {})
    #return render(request, 'paieelApp/reconocimiento.html', {})

def send_command(request):
    commando = ["./util/align-dlib.py", "./training-images/", "align", "outerEyesAndNose", "./aligned-images/",
                "--size", "96"]
    proc = subprocess.Popen(commando, cwd="/home/pamela/Escritorio/openface", stdout=subprocess.PIPE)
    out = proc.communicate()
    print out[0]

    commando2 = ["./batch-represent/main.lua", "-outDir", "./generated-embeddings/", "-data", "./aligned-images/"]
    proc2 = subprocess.Popen(commando2, cwd="/home/pamela/Escritorio/openface", stdout=subprocess.PIPE)
    out2 = proc2.communicate()
    print out2[0]

    commando3 = ["./demos/classifier.py", "train", "./generated-embeddings/"]
    proc3 = subprocess.Popen(commando3, cwd="/home/pamela/Escritorio/openface", stdout=subprocess.PIPE)
    out3 = proc3.communicate()
    print out3[0]

    return render(request, 'paieelApp/reconocimiento.html', {})
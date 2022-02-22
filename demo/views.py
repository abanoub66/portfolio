import os.path
import subprocess
from os import listdir
from os.path import isfile, join
from subprocess import STDOUT, PIPE

from django.shortcuts import render, redirect

from .models import Demo

java_file_path = 'demo/JavaSortingMethods'


def number_list_create(request):
    if request.method == 'POST':
        size = int(request.POST['index']) + 1
        data = ''
        for i in range(size):
            if request.POST['index' + str(i)] != '':
                data += request.POST['index' + str(i)] + ', '
        data = data[:-2]
        for i in Demo.objects.all():
            if i.number_list == data:
                return redirect('sorting_list', current=data)
        instance = Demo.objects.create(number_list=data)
        instance.save()
        return redirect('sorting_list', current=instance.number_list)
    return render(request, "demo/number_list_create.html")


def sorting_list(request, current):
    sorts = [f for f in listdir(java_file_path) if isfile(join(java_file_path, f))]
    files = []
    for s in sorts:
        filename, ext = os.path.splitext(s)
        if ext == '.java' and filename != 'Main':
            files.append(filename)
    return render(request, "demo/sorting_list.html", {'sorts': files, 'current': current})


def sort(request, current, s):
    os.chdir(java_file_path)
    cmd = ['java', '-classpath', '.', 'Main'] + [s, current]
    proc = subprocess.Popen(cmd, stdin=PIPE, stdout=PIPE, stderr=STDOUT)
    stdout, stderr = proc.communicate()
    os.chdir('..\\..')
    display = stdout.decode('UTF-8')
    return render(request, "demo/sort_anim.html", {'current': current, 'sort': s, 'display': display})


def previous_demos(request):
    demos = Demo.objects.all()
    return render(request, "demo/previous_demos.html", {'demos': demos})


def about(request):
    return render(request, "about.html")

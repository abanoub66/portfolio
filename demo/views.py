import os.path
import subprocess
import re
from os import listdir
from os.path import isfile, join
from subprocess import STDOUT, PIPE

from django.shortcuts import render, redirect

from .models import Demo

java_file_path = 'demo\\JavaSortingMethods'


def number_list_create(request):
    if request.method == 'POST':
        size = int(request.POST['index']) + 1
        data = ''
        for i in range(size):
            data += request.POST['index' + str(i)] + ', '
        data = data[:-2]
        instance = Demo.objects.create(number_list=data)
        instance.save()
        return redirect('sorting_list', current=instance.number_list)
    return render(request, "demo/number_list_create.html")


def sorting_list(request, current):
    sorts = [f for f in listdir(java_file_path) if isfile(join(java_file_path, f))]
    for s in sorts:
        if re.search('java$', s):
            sorts.remove(s)
            sorts.append(s.removesuffix('.java'))
    return render(request, "demo/sorting_list.html", {'sorts': sorts, 'current': current})


def sort(request, current, s):
    j = java_file_path + '\\' + s + '.java'
    subprocess.check_call(['javac', j])
    cmd = ['java', '-classpath', '.\\demo\\JavaSortingMethods', s] + [current]
    proc = subprocess.Popen(cmd, stdin=PIPE, stdout=PIPE, stderr=STDOUT)
    stdout, stderr = proc.communicate()
    display = stdout.decode('UTF-8')
    j = j.replace('.java', '.class')
    if os.path.isfile(j):
        os.remove(j)
    return render(request, "demo/sort_anim.html", {'current': current, 'sort': s, 'display': display})


def previous_demos(request):
    demos = Demo.objects.all()
    return render(request, "demo/previous_demos.html", {'demos': demos})


def about(request):
    return render(request, "about.html")

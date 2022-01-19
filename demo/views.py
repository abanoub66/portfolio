import os.path
import subprocess
from os import listdir
from os.path import isfile, join
from subprocess import STDOUT, PIPE

from django.shortcuts import render, redirect

from . import forms
from .models import Demo

java_file_path = 'R:\\farag\\PyCharmProjects\\portfolio\\demo\\JavaSortingMethods'


def number_list_create(request):
    if request.method == 'POST':
        form = forms.CreateNumberList(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect('sorting_list', current=instance.number_list)
    else:
        form = forms.CreateNumberList()
    return render(request, "demo/number_list_create.html", {'form': form})


def sorting_list(request, current):
    sorts = [f for f in listdir(java_file_path) if isfile(join(java_file_path, f))]
    return render(request, "demo/sorting_list.html", {'sorts': sorts, 'current': current})


def sort(request, current, s):
    subprocess.check_call(['javac', java_file_path + '\\' + s])
    java_class, ext = os.path.splitext(java_file_path + '\\' + s)
    cmd = ['java', java_class]
    proc = subprocess.Popen(cmd, stdin=PIPE, stdout=PIPE, stderr=STDOUT)
    stdout, stderr = proc.communicate()
    print('This was "' + stdout.decode('UTF-8') + '"')
    return render(request, "demo/sort_anim.html", {'current': current, s: 's'})


def previous_demos(request):
    demos = Demo.objects.all()
    return render(request, "demo/previous_demos.html", {'demos': demos})

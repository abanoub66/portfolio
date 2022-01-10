from django.shortcuts import render, redirect
from .models import Demo
from . import forms
from os import listdir
from os.path import isfile, join


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
    my_path = 'R:\\farag\\PyCharmProjects\\portfolio\\demo\\JavaSortingMethods'
    sorts = [f for f in listdir(my_path) if isfile(join(my_path, f))]
    return render(request, "demo/sorting_list.html", {'sorts': sorts, 'current': current})


def previous_demos(request):
    demos = Demo.objects.all()
    return render(request, "demo/previous_demos.html", {'demos': demos})

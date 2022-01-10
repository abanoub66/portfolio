from django.shortcuts import render, redirect
from .models import Demo, SortingMethod
from . import forms


# Create your views here.

def number_list_create(request):
    if request.method == 'POST':
        form = forms.CreateNumberList(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect('sorting_list')
    else:
        form = forms.CreateNumberList()
    return render(request, "demo/number_list_create.html", {'form': form})


def sorting_list(request):
    sorts = SortingMethod.objects.all().order_by('sorting_method')
    return render(request, "demo/sorting_list.html", {'sorts': sorts})


def previous_demos(request):
    demos = Demo.objects.all()
    return render(request, "demo/previous_demos.html", {'demos': demos})

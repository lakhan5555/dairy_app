from django.shortcuts import render, redirect
from .models import *
from .forms import EntryForm

from django.contrib import messages

def index(request):
    
    entries = Entry.objects.order_by('-date_posted')

    context = {
        'entries' : entries
    }
    return render(request,'index.html', context)


def add(request):

        if request.method == 'POST':
            form = EntryForm(request.POST)
            if form.is_valid():
               form.save()
               return redirect('index')
        else:
            form = EntryForm

        context = { 'form': form}
        return render(request,'add.html', context)


from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .forms import SystemForm
from .models import *


def index(request):
    if request.method == 'POST':
        form = SystemForm(request.POST)
        if form.is_valid():
            prop = Proposal(text = form.cleaned_data['text'])
            prop.save()
    props = Proposal.objects.all()
    return render(request,'main.html',{'props':props})

def submit(request):
    form = SystemForm()
    return render(request, 'submit.html',{'form':form})

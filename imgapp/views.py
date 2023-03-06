from django.shortcuts import render
from imgapp.forms import imgform
from imgapp.models import imgmodel

# Create your views here.
def index(request):
    form = imgform()
    if request.method == 'POST':
        form = imgform(request.POST,request.FILES)
        if form.is_valid():
            form.save()
    return render(request,'index.html',{'form':form})

def display(request):
    images=imgmodel.objects.all()
    return render(request,'display.html',{'images':images})

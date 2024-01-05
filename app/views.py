from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from app.forms import *

def djforms(request):
    ENFO=NameForm()
    d={'ENFO':ENFO}


    if request.method=='POST':
        NFDO=NameForm(request.POST)
        if NFDO.is_valid():
            return HttpResponse(str(NFDO.cleaned_data))

        else:
            return HttpResponse('Data is not Valid')

    return render(request,'djforms.html',d)
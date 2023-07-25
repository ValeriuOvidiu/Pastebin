from django.http import HttpResponse
from django.shortcuts import render
from .models import textInput


def index(request):
    context = {
    'n': reversed(textInput.objects.all()),   
        }

    return render(request,"TextProcesing/index.html",context)

def createpost(request):   
        if request.method == 'POST':
            if  request.POST.get('content'):
                post=textInput()
                post.textSaved = request.POST.get('content')
                print(len(post.textSaved))
                post.save()   
                context = {
    'n':reversed(textInput.objects.all()),   
        }  
                return render(request, 'TextProcesing/index.html',context)  

        
        context = {
        'n':reversed(textInput.objects.all()),   
            }
        return render(request, 'TextProcesing/index.html',context) 
 
def layout(request, id1 ):
     context = {
    'text': textInput.objects.get(id=id1),   
        }  
     if(request.method=="GET"):
        return render (request, 'TextProcesing/layout.html',context)     


from django.shortcuts import render, HttpResponse


def index(request):
   #context = {
    #   "x" : "this is sent"
    #}
    return HttpResponse('this is home.') 
   # return render(request, 'index.html', context)
    
def about(request):
    return HttpResponse('this is about page.')

def services(request):
    return HttpResponse('this is services page.')

def contact(request):
    return HttpResponse('this is contact page.')
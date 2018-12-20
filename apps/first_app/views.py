from django.shortcuts import render, HttpResponse

#def index(request):
    #return HttpResponse("portfolio")

def index(request):
    return render(request, 'first_app/index.html')




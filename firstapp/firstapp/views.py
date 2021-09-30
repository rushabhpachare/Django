from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    params = {'name' : 'Rushabh', 'place': 'India'}
    return render(request, 'index.html', params)


def removepunc(request):
    #Get the text
    djtext = request.GET.get('text', 'default')
    print(djtext)
    #Analyze the text
    return HttpResponse('''removepunc <br/> <a href="/"> Back </a>''')


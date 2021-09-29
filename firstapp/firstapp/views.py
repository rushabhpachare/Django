from django.http import HttpResponse


def index(request):
    return HttpResponse('''<h1>One Batch Two Batch <br/> Link for the websites <br/><a href="https://www.netflix.com/in/"> NETFLIX </a>  <br/><a href="https://www.hotstar.com/in"> HOTSTAR </a>  <br/><a href="https://www.google.com/">GOOGLE</a>  </h1> <br/> <h3> Go to next page and back button </h3> <br/> <h3> <a href="/removepunc"> Remove Punc </a><br/>  <a href="/capitalizefirst"> Capitalize First </a><br/>  <a href="/newlineremove"> New Line Remove </a><br/>  <a href="/spaceremove"> Space Remove </a><br/>  <a href="/charcount"> Char Count </a><br/>  </h3>''')


def about(request):
    return HttpResponse('''<h3>Penny and Dime  <br/><a href="https://www.marvel.com/tv-shows/marvel-s-daredevil/3"> DAREDEVIL </a>  <br/><a href="https://www.netflix.com/in/title/80002566"> DEFENDERS </a>  <br/><a href="https://www.netflix.com/in/title/80002612"> IRON FIST</a>  </h3>''')


def removepunc(request):
    return HttpResponse('''removepunc <br/> <a href="/"> Back </a>''')

def capitalizefirst(request):
    return HttpResponse('''capitalizefirst <br/> <a href="/"> Back </a>''')

def newlineremove(request):
    return HttpResponse('''newlineremove <br/> <a href="/"> Back </a>''')

def spaceremove(request):
    return HttpResponse('''spaceremove <br/> <a href="/"> Back </a>''')

def charcount(request):
    return HttpResponse('''charcount <br/> <a href="/"> Back </a>''')
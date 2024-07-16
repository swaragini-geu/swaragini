from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')
    #return HttpResponse("this is about page")

def dance(request):
    return render(request,'dance.html')
    #return HttpResponse("this is dance page")

def contact(request):
    return render(request,'contact.html')

def music(request):
    return render(request, 'music.html')
    #return HttpResponse("this is music page")

def core_team_view(request):
    return render(request, 'core.html')

def gallery(request):
    return render(request,'gallery.html')
    #return HttpResponse("this is gallery page")
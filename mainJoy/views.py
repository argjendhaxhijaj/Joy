from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import Post
from .models import kursi
from .models import njoftimet
from .forms import PostForm
from django.contrib.auth.decorators import login_required
# Create your views here.


def home(request):
    return render(request, 'joy/ballina.html')

def about(request):
    return render(request, 'joy/per.html')

#def log(request):
    #return render(request, 'joy/kyqu.html')

#def register(request):
 #   return render(request, 'joy/regjistrohu.html')

def chance(request):

    context = {
        'posts': Post.objects.all().order_by('-date_posted')
      
    }

    return render(request, 'joy/qellimi.html', context)


@login_required
def createpost(request):
        if request.method == 'POST':
            if request.POST.get('first_name') and request.POST.get('last_name') and request.POST.get('title') and request.POST.get('content') and request.POST.get('document') and request.POST.get('url'):
              post=njoftimet()
              post.first_name= request.POST.get('first_name')
              post.last_name= request.POST.get('last_name')
              post.title= request.POST.get('title')
              post.content= request.POST.get('content')
              post.document= request.POST.get('document')
              post.url= request.POST.get('url')
              post.save()
              return render(request, 'joy/kontakti.html')  

        else:
            return render(request,'joy/kontakti.html')


@login_required
def home1(request):
    return render(request, 'joy/ballina1.html')

@login_required
def cinema(request):
    return render(request, 'joy/kinemaja.html')

@login_required
def course(request):
    template = 'joy/kursi.html'
    Animacion = kursi.objects.filter(titulli="Animacion")
    con = {
    'course': Animacion
    }
    return render(request, template, con)

@login_required
def course1(request):
    template = 'joy/kursi1.html'
    Frontend = kursi.objects.filter(titulli="Frontend")
    con = {
    'course': Frontend
    }
    return render(request, template, con)

@login_required
def course2(request):
    template = 'joy/kursi2.html'
    Python = kursi.objects.filter(titulli="Python")
    con = {
    'course': Python
    }
    return render(request, template, con)

@login_required
def course3(request):
    template = 'joy/kursi3.html'
    JavaScript = kursi.objects.filter(titulli="JavaScript")
    con = {
    'course': JavaScript
    }
    return render(request, template, con)

@login_required
def course4(request):
    template = 'joy/kursi4.html'
    Blender = kursi.objects.filter(titulli="Blender")
    con = {
    'course': Blender
    }
    return render(request, template, con)

#def course(request):
#    con = {
#        'course': kursi.objects.all()
      
#    }
#    return render(request, 'joy/kursi.html', con)

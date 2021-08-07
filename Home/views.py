from django.shortcuts import render, HttpResponse, redirect,HttpResponseRedirect

from Home.models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# Create your views here.

def home(request):
    category = request.GET.get('category')
    if category == None:
       photos = Photo.objects.all()
    else:
        photos = Photo.objects.filter(Category__name=category)  
   

    categories = Category.objects.all()
    
    # photos = Photo.objects.all()
    
    context = {'cata': categories, 'poths':photos}



    return render(request, 'home/home.html',context)

def addphotos(request):
    try:
        categories = Category.objects.all()
        
        if request.method == 'POST':


            catery = request.POST.get('category')
            catery_new = request.POST.get('Category_new')
            image = request.FILES.getlist('image')

            if catery != 'none':
                category = Category.objects.get(id=catery)
            elif catery_new  != '':
                category , create = Category.objects.get_or_create(name=catery_new)
            else:
                category = None
            for img in image:
                photo = Photo.objects.create(
                    Category = category,
            
                    image = img,
                )
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        
        
    except Exception as e:
        print(e)
    
 
    return render(request, 'home/addphotos.html',{'cata': categories})


def photov(request, pk):
    categories = Category.objects.all()
    photo = Photo.objects.get(id=pk)
    
   
    context = {'photos':photo,'cata': categories}
    print(context)
    return render(request, 'home/photoview.html', context)

def deletev(request, pk):
  

    delete = Photo.objects.get(id=pk)
    delete.delete()
   
    
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
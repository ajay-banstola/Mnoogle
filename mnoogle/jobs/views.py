from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Jobs
from .forms import *
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpRequest, HttpResponseRedirect
from django.db.models import Count
# Create your views here.

def list_jobs(request, category_slug=None):
    search_term = ''
    category = None
    users = User.objects.exclude(id=request.user.id)
    jobs_list = Jobs.objects.all()
    
    #jobs_list = paginator.get_page(page)
    query = request.GET.get('q')
    if query=='':
        return HttpResponseRedirect('/')
    if query:
        jobs_list = Jobs.objects.filter(Q(Job__icontains=query)| Q(URL__icontains=query)).order_by("-Deadline")

    paginator = Paginator(jobs_list,3)
    page = request.GET.get('page',10)
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    jobs_counter = jobs_list.annotate(Count('id'))
    jobs_count = len(jobs_counter)        

    context = {
        'products':products,
        'jobs_list':jobs_list,
        'jobs_count':jobs_count,
        'query':query,
        'users':users,
        'category':category,
        'search_term':search_term
    }
    return render(request, 'jobs/product/list.html',context)

def pinned(request,category_slug=None):
        #request.GET.get('pinned'):
    users = User.objects.exclude(id=request.user.id)
    #if request.method =='POST':
    jobs_list1 = Jobs.objects.all()

    if request.method =="POST":
        vari = request.POST.get('number')
        vari = int(vari)
        for evert in jobs_list1:
            vari1 = evert.Job_Id
            if (vari == vari1):
                checkvar1 = request.POST.get('unpin') or request.POST.get('pin')
                if (checkvar1=="Pin"):
                    print(checkvar1)
                    evert.flag = True
                if (checkvar1 =="Unpin"):
                    print(checkvar1)
                    evert.flag = False
                evert.save(update_fields=["flag"])
            
    return HttpResponseRedirect('/account/profile')
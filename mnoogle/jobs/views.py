from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Jobs
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpRequest, HttpResponseRedirect
from django.db.models import Count
# Create your views here.
def list_jobs(request, category_slug=None):
    users = User.objects.exclude(id=request.user.id)
    jobs_list = Jobs.objects.all()
    query = request.GET.get('q')
    if query=='':
        return HttpResponseRedirect('/')
    if query:
        jobs_list = Jobs.objects.filter(Q(slug__icontains=query)| Q(Link__icontains=query)).order_by("-Deadline")

    jobs_counter = jobs_list.annotate(Count('id'))
    jobs_count = len(jobs_counter)        

    context = {
        'jobs_list':jobs_list,
        'jobs_count':jobs_count,
        'query':query,
        'users':users,
    }
    return render(request, 'jobs/product/list.html',context)


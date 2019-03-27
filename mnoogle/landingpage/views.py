from django.shortcuts import render

from django.http import HttpResponse

app_name = 'landingpage'


def landingpage(request):
    return render(request, 'landingpage/landing_page.html')
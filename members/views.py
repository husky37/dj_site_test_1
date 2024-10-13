from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.


def members(request):
    template = loader.get_template('members_list.html')
    return HttpResponse(template.render())


def page_not_found_views(request, exception):
    return render(request, '404.html', status=404)

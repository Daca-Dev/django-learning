from django.http import HttpRequest
from django.shortcuts import render


def index(request: HttpRequest):
    """example of a view function"""
    # we extract the name of queryParam (QueryDict) and apply a default value with or statement
    # because es posible that if the name comming that return an empty string that is valid if
    # the user send it
    name = request.GET.get('name') or "world"
    context = {
        'name': name,
    }
    return render(request, 'base.html', context)

def search(request: HttpRequest):
    """example of a view function"""
    search_term = request.GET.get('search') or "-- Nothing --"
    
    return render(request, 'search.html', {
        "search_term": search_term,
    })
    

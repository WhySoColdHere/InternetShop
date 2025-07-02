from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect, get_object_or_404

header_menu = [
    {'title': "About site", 'url_name': "index"},
    {'title': "FAQ", 'url_name': "index"},
    {'title': "Feedback", 'url_name': "index"},
]

footer_menu = [
    {'title': "Some..info?", 'url_name': "index"},
]


def index(request):
    data = {
        'header_menu': header_menu,
        'footer_menu': footer_menu,
    }
    return render(request, 'shop/index.html', data)


def page_not_found(request, exception):
    return HttpResponseNotFound('custom 404 err')

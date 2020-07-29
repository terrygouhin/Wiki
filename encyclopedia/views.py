from django.http import HttpResponse
from django.shortcuts import render

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })
    
def Oldentry(request, entry):
    return render(request, "encyclopedia/entry.html", {
        "ShowEntry": util.get_entry({entry})
    })


def entry(request, title):
    return render(request, "encyclopedia/entry.html", {
        "title": util.get_entry({title})
    })
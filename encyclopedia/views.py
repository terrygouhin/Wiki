from django.http import HttpResponse
from django.shortcuts import render
from markdown2 import markdown, markdown_path

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })
    
def css(request):
    html = markdown_path("entries/css.md")
    return HttpResponse(html)
    
def GetEntry(request, title):
    text = util.get_entry(title)
    if text is None:
        html = markdown_path("encyclopedia/templates/encyclopedia/Not Found.md")
        return render(request, "encyclopedia/notFound.html", {"html": html, "title": title})
    else:
        html = markdown(text)
        return render(request, "encyclopedia/entry.html", {"html": html, "title": title})


def entry(request, title):
    entryPath = "entries/"+title+".md"
    html = markdown_path("entries/"+title+".md")
    return HttpResponse({html})
    
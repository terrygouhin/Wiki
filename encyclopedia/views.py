from django.http import HttpResponse
from django.shortcuts import render
from markdown2 import markdown, markdown_path

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })
    
def GetEntry(request, entry):
    text = util.get_entry(entry)
    if text is None:
        html = markdown_path("encyclopedia/templates/encyclopedia/Not Found.md")
        return render(request, "encyclopedia/notFound.html", {"html": html, "entry": entry})
    else:
        html = markdown(text)
        return render(request, "encyclopedia/entry.html", {"html": html, "entry": entry})


    
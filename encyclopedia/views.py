from django import forms
from django.shortcuts import render
from markdown2 import markdown, markdown_path
from django.core.files import File

from . import util

class NewEntryForm(forms.Form):
    title =  forms.CharField(label="New Entry Title")
    mdText = forms.CharField(widget=forms.Textarea(attrs={'id':'mdText', 'name':'mdText', 'rows':'5', 'cols':'25'})) 

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
        
def newentry(request):
    if request.method=="POST":
        form = NewEntryForm(request.POST)
        if form.is_valid():
            NewEntry = form.cleaned_data["mdText"]
            title = form.cleaned_data["title"]
            filename='entries/'+title+'.md'
            f = open(filename, 'w+')
            f.write(NewEntry)
            f.close()
        else:
            return render(request, "encyclopedia/NewEntry.html", {
                "form":form
            })
            
    return render(request, "encyclopedia/NewEntry.html", {
        "form": NewEntryForm()
    })


    
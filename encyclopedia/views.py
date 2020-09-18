from django import forms
from django.shortcuts import render
from markdown2 import markdown, markdown_path
from django.core.files import File

from . import util

class NewEntryForm(forms.Form):
    title =  forms.CharField(label="Entry Title")
    mdText = forms.CharField(widget=forms.Textarea(attrs={'id':'mdText', 'name':'mdText'})) 

class EditEntryForm(forms.Form):
    entry =  forms.CharField(label="Entry Title")
    content = forms.CharField(widget=forms.Textarea(attrs={'id':'editText', 'name':'editText', 'value':'content'})) 

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
            content = form.cleaned_data["mdText"]
            title = form.cleaned_data["title"]
            util.save_entry(title, content)
        else:
            return render(request, "encyclopedia/NewEntry.html", {
                "form":form
            })
            
    return render(request, "encyclopedia/NewEntry.html", {
        "form": NewEntryForm()
    })

def dispentry(request, entry):
    text = util.get_entry(entry)
    return render(request, "encyclopedia/editEntry2.html", {"entry": entry})
    if request.method =="POST":
        if form.is_valid():
            content = form.cleaned_data["editText"]
            title = form.cleaned_data["entry"]
            util.save_entry(title, content)
        else:
            return HttpResponse ("Invalid data")  
    data = {"title":"{{entry}}", "content":"mycontent"}        

def editentry(request, entry):
    content = util.get_entry(entry)
    data = {'entry':entry, 'content':content}
    form = EditEntryForm(data, initial=data)
    
    return render(request, "encyclopedia/editEntry.html", {
        "form":form, "entry":entry
    })

    
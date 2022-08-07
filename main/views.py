from re import L
from unicodedata import name
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDoList, Item, Url
from .forms import CreateNewList
# Create your views here.


def index(response, id):
    ls = ToDoList.objects.get(id=id)

    if response.method == "POST":
        print(response.POST)
        if response.POST.get("save"):
            for item in ls.item_set.all():
                if response.POST.get("c" + str(item.id)) == 'clicked':
                    item.complete == True
                else:
                    item.complete == False

                item.save()

        elif response.POST.get("newItem"):
            txt = response.POST.get('newI')
            if len(txt) > 2:
                ls.item_set.create(text=txt, complete=True)
            else:
                print("invalid")

        elif response.POST.get("newUrl"):
            txt = response.POST.get('newU')
            if len(txt) > 2:
                ls.url_set.create(text=txt, complete=True)
            else:
                print("invalid")

    return render(response, "main/list.html", {"ls": ls})


def home(response):
    ls = ToDoList.objects
    return render(response, "main/home.html", {"ls": ls})


def create(response):
    if response.method == "POST":
        form = CreateNewList(response.POST)

        if form.is_valid():
            n = form.cleaned_data["name"]
            t = ToDoList(name=n)
            t.save()

        return HttpResponseRedirect("/%i" % t.id)
    else:
        form = CreateNewList()
    return render(response, "main/create.html", {"form": form})

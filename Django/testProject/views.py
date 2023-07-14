from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'base.html', {})


def contacts(request, *ags, **kwargs):
    # return HttpResponse("<h1>Contacts</h1>")
    my_context = {
        "my_list": ["Abc", 123]
    }
    return render(request, 'contacts.html', my_context)


def about(request, *ags, **kwargs):
    # return HttpResponse("<h1>About</h1>")
    my_context = {
        "my_text": "This is my_text.",
        "my_number": 1234
    }
    return render(request, 'about.html', my_context)

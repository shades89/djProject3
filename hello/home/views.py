from django.shortcuts import render, HttpResponse


def index(request):
    context = {
        "variable":"this is sent"
    }
    # return HttpResponse("This is the Homepage", request)
    return render(request, 'index.html', context)


def about(request):
    return render(request, 'about.html')
    # return HttpResponse("This is the About Page", request)


def services(request):
    return render(request, 'services.html')
    # return HttpResponse("This is the Services Page", request)


def contacts(request):
    return render(request, 'contacts.html')
    # return HttpResponse("This is the Contacts Page", request)

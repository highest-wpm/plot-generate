from django.shortcuts import render
# from django.http import HttpResponse


# Create your views here.


def index(request):
    ggyy = {"ggyy": "Something passed through context."}
    return render(request, "../templates/plot_generate/index.html", context=ggyy)

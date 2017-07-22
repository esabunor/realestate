from django.shortcuts import render

def search_view(request):
    return render(request, "search.html")

def result_view(request):
    return render(request, "results.html")
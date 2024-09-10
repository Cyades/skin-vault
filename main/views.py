from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2306152430',
        'name': 'Malvin Scafi',
        'class': 'PBP F'
    }

    return render(request, "main.html", context)
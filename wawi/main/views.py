from django.shortcuts import render

# Create your views here.

def home(request):
    title = 'الصفحة الرئيسية'
    return render(request, 'home.html', {'title': title})

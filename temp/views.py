from django.shortcuts import render

# Create your views here.
def index(request):
    
    return render(request,"pages/index-page.html")

def category(request):
    
    return render(request,"pages/category.html")
def archive(request):
    
    return render(request,"pages/archive.html")
def blog(request):
    
    return render(request,"pages/blog-details.html")

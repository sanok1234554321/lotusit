from django.shortcuts import render

# Create your views here.

def main_page(request):
    return render(request,"index.html")

def categories(request):
    return render(request,"categories.html")

def community(request):
    return render(request,"community.html")

def contact(request):
    return render(request,"contact.html")

def review(request):
    return render(request,"review.html")

def single_blog(request):
    return render(request,"single-blog.html")
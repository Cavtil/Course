from django.shortcuts import render



def about_hendler(request):
    context = {}
    return render(request, 'news/about.html', context)

def contact_hendler(request):
    context = {}
    return render(request, 'news/contact.html', context)

def elements_hendler(request):
    context = {}
    return render(request, 'news/elements.html', context)

def index_hendler(request):
    context = {}
    return render(request, 'news/index.html', context)

def main_hendler(request):
    context = {}
    return render(request, 'news/main.html', context)

def property_hendler(request):
    context = {}
    return render(request, 'news/property.html', context)

def blog_hendler(request):
    context = {}
    return render(request, 'news/blog.html', context)

def robots_hendler(request):
    context = {}
    return render(request, 'news/robots.txt', context, content_type='text/plain')












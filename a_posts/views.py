from django.shortcuts import render

def home_view(request):
    title = 'welcome to django'
    return render(request, 'a_posts/home.html', {'title' : title})
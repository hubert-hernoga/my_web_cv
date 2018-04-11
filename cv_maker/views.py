from django.views import View
from django.shortcuts import render


class TitlePage(View):
    def get(self, request):
        pass
        return render(request, 'multipage/index-eng.html')


class Project(View):
    def get(self, request):
        pass
        return render(request, 'multipage/project.html')


class CoverLatter(View):
    def get(self, request):
        pass
        return render(request, 'multipage/cover-latter-eng.html')


class Blog(View):
    def get(self, request):
        pass
        return render(request, 'multipage/blog_eng.html')


class BlogPost(View):
    def get(self, request):
        pass
        return render(request, 'multipage/blog-full-post-eng.html')


class Contact(View):
    def get(self, request):
        pass
        return render(request, 'multipage/contact-eng.html')


class Portfolio(View):
    def get(self, request):
        pass
        return render(request, 'multipage/portfolio-full.html')
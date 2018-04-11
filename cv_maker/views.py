from django.views import View
from django.shortcuts import render


class TitlePage(View):
    def get(self, request):
        pass
        return render(request, 'multipage/pl/index-pl.html')


class Project(View):
    def get(self, request):
        pass
        return render(request, 'multipage/project.html')


class CoverLatter(View):
    def get(self, request):
        pass
        return render(request, 'multipage/pl/cover-latter-pl.html')


class Blog(View):
    def get(self, request):
        pass
        return render(request, 'multipage/pl/blog_pl.html')


class BlogPost(View):
    def get(self, request):
        pass
        return render(request, 'multipage/pl/blog-full-post-pl.html')


class Contact(View):
    def get(self, request):
        pass
        return render(request, 'multipage/pl/contact-pl.html')


class Portfolio(View):
    def get(self, request):
        pass
        return render(request, 'multipage/pl/portfolio-full.html')
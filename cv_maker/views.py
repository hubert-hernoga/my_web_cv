from django.views import View
from django.shortcuts import render


class TitlePage(View):
    def get(self, request):
        pass
        return render(request, 'multipage/index.html')


class Project(View):
    def get(self, request):
        pass
        return render(request, 'multipage/project.html')


class CoverLatter(View):
    def get(self, request):
        pass
        return render(request, 'multipage/cover-latter.html')


class Blog(View):
    def get(self, request):
        pass
        return render(request, 'multipage/blog.html')


class BlogPost(View):
    def get(self, request):
        pass
        return render(request, 'multipage/blog-full-post.html')


class Contact(View):
    def get(self, request):
        pass
        return render(request, 'multipage/contact.html')


class Portfolio(View):
    def get(self, request):
        pass
        return render(request, 'multipage/portfolio-full.html')
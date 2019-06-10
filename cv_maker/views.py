from django.views import View
from django.shortcuts import render


class TitlePage(View):
    def get(self, request):
        return render(request, 'multipage/index.html')


class CoverLatter(View):
    def get(self, request):
        pass
        return render(request, 'multipage/cover-letter.html')


class Projects(View):
    def get(self, request):
        pass
        return render(request, 'multipage/projects.html')


class ProjectShop(View):
    def get(self, request):
        pass
        return render(request, 'multipage/project-shop.html')

class ProjectCV(View):
    def get(self, request):
        pass
        return render(request, 'multipage/project-cv.html')

class LaSante(View):
    def get(self, request):
        pass
        return render(request, 'multipage/lasante.html')

class InterDrinks(View):
    def get(self, request):
        pass
        return render(request, 'multipage/interdrinks.html')

class FrenchTouch(View):
    def get(self, request):
        pass
        return render(request, 'multipage/french_touch.html')

class Contact(View):
    def get(self, request):
        pass
        return render(request, 'multipage/contact.html')


class Portfolio(View):
    def get(self, request):
        pass
        return render(request, 'multipage/portfolio-full.html')


class Blog(View):
    def get(self, request):
        pass
        return render(request, 'multipage/blog.html')
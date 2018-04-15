from django.views import View
from django.shortcuts import render
import pyautogui
import cloudconvert
import os
from urllib.request import urlopen

class TitlePage(View):
    def get(self, request):
        return render(request, 'multipage/index.html')


class GeneratorPDF(View):
    def get(self, request):
        api = cloudconvert.Api(os.environ['CV_CONVERT_API'])
        scr = pyautogui.screenshot()
        scr.save('scr.png')

        process = api.convert({
            'inputformat': 'png',
            'outputformat': 'pdf',
            'input': 'upload',
            'file': open('scr.png', 'rb')
        })
        process.wait()
        process.download("scr.pdf")

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
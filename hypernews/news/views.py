import datetime
import json
from random import randint
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.base import View


def home(request):
    return redirect('/news')


class MainView(View):

    def get(self, request, *args, **kwargs):
        with open("C:\\pythonProject\\HyperNews Portal\\task\\news.json", "r") as json_file:
            list_json = json.load(json_file)
        search_item = request.GET.get('q')
        if search_item:
            list_json = [item for item in list_json if search_item in item.get('title')]
            return render(request, "news/mainpage.html", context={'list_json': list_json})
        return render(request, "news/mainpage.html", context={'list_json': list_json})


class ArticleView(View):

    def get(self, request, *args, **kwargs):
        global sac
        with open("C:\\pythonProject\\HyperNews Portal\\task\\news.json", "r") as json_file:
            list_json = json.load(json_file)
        for i in range(len(list_json)):
            if list_json[i].get('link') == int(kwargs['link']):
                sac = {"post": list_json[i]}
                return render(request, "news/index.html", context=sac)
        else:
            return HttpResponse("<h1>No such page</h1>")


class CreateArticle(View):
    new_article_dict = {}

    def get(self, request):
        return render(request, "news/create.html")

    def post(self, request):
        title = request.POST.get('title')
        text = request.POST.get('text')
        created = datetime.datetime.now()
        link = randint(5, 1000)
        self.new_article_dict["created"] = str(created)[:-7]
        self.new_article_dict["text"] = text
        self.new_article_dict["title"] = title
        self.new_article_dict["link"] = link
        with open("C:\\pythonProject\\HyperNews Portal\\task\\news.json", "r") as json_file:
            list_json = json.load(json_file)
        list_json.append(self.new_article_dict)
        with open("C:\\pythonProject\\HyperNews Portal\\task\\news.json", "w") as j:
            json.dump(list_json, j)
        return redirect('/news/')






from main import models
from django.shortcuts import render, redirect
def isOwner(func):
    def wrapper(request, id , *args, **kwargs):
        obj = models.Blog.objects.get(id=id)
        if obj.author == request.user:
            return func(request, id, *args, **kwargs)
        else:
             return redirect('index')
    return wrapper

#  https://github.com/AxliddinShokirov/7-oy-decorators.git
   






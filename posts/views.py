from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,get_object_or_404,redirect
from django.db import models
from django.http import HttpResponse,HttpResponseRedirect

from posts.models import Post

# Create your views here.
from posts.forms import PostForm


from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render




def post_create(request):

    form = PostForm(request.POST or None,request.FILES or None)

    if form.is_valid():


        instance=form.save(commit=False)

        instance.save()
        messages.success(request,"Successfully Posted")
        return HttpResponseRedirect(instance.get_absolute_url())


    context={

        "form":form,
        "title":"create view",
    }
    return render(request,"postform.html",context)


def post_home(request):

    qset=Post.objects.all().order_by('-timestamp')
    paginator = Paginator(qset, 10)  # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        queryset = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        queryset = paginator.page(paginator.num_pages)

    context={
        "object_list":queryset,
        "title":"list"
    }
    return render(request,"base.html",context)


def post_update(request,id=None):
    print id
    instance = get_object_or_404(Post, id=id)
    form=PostForm(request.POST or None,request.FILES or None, instance=instance)
    print "one"
    if form.is_valid():
        instance=form.save(commit=False)
        instance.save()

        messages.success(request, "Successfully Posted")
        return HttpResponseRedirect(instance.get_absolute_url())

    context = {
        "form": form,
        "title": "update view",

    }
    return render(request, "postform.html", context)

def post_detail(request,id=None):


    qset=get_object_or_404(Post,id=id)

    context={
        "obj":qset,
        "title":"list"
    }
    return render(request,"detail.html",context)

def post_delete(request,id=None):

    instance=get_object_or_404(Post,id=id)
    instance.delete()
    messages.success(request,"Deleted your post")
    return  redirect("posts")




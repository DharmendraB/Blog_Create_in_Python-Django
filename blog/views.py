from django.shortcuts import render
from blog.models import Blogpost

# Create your views here.
def blogHome(request):
    AllBlogs = Blogpost.objects.order_by('-post_id')    
    params = {'allpost':AllBlogs} 
    return render(request, 'blog/blog.html',params)

def blogPost(request,id,slug):
    post = Blogpost.objects.filter(post_id = id).first()
    return render(request, 'blog/blogpost.html',{'post':post})
from django.http.response import HttpResponse
from django.shortcuts import render

data = {
    "blogs": [
        {
            "id":1,
            "title":"Web Development",
            "image":"web.jpg",
            "is_active":True,
            "is_home":True,
            "description":"The Course you looked for"
        },
        
        {
            "id":2,
            "title":"Web Development",
            "image":"web.jpg",
            "is_active":True,
            "is_home":False,
            "description":"The Course you looked for"
        },
        
        {
            "id":3,
            "title":"Web Development",
            "image":"web.jpg",
            "is_active":True,
            "is_home":True,
            "description":"The Course you looked for"
        },
        
        {
            "id":4,
            "title":"Web Development",
            "image":"web.jpg",
            "is_active":False,
            "is_home":True,
            "description":"The Course you looked for"
        },
        
        {
            "id":5,
            "title":"Web Development",
            "image":"web.jpg",
            "is_active":True,
            "is_home":True,
            "description":"The Course you looked for"
        },
    ]
}

def index(request):
    context = {
        "blogs":data["blogs"]
    }
    return render(request, "app/index.html", context)

def blogs(request):
    context = {
        "blogs":data["blogs"]
    }
    return render(request, "app/blogs.html",context)

def blog_details(request, id):
 
    
    blogs = data["blogs"]
    selectedBlog = [blog for blog in blogs if blog["id"] == id][0]
    return render(request, "app/blog-details.html", {
        "blog": selectedBlog
    })

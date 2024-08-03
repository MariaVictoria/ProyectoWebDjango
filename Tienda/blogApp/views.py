from django.shortcuts import render
from blogApp.models import Post, Categoria
def blog(request):
    posts = Post.objects.all()
    return render(request, 'blogApp/blog.html', {'posts': posts})

def categoria(request, categoria_id):
    categorias=Categoria.objects.get(id=categoria_id)
    posts = Post.objects.filter(categorias=categorias)
    return render (request ,'blogApp/categoria.html', {'categorias':categorias, 'posts':posts})

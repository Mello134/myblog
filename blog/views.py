from django.shortcuts import render, get_object_or_404#404 - покажет либо нужный объект, а если его нет покажет 404
from . models import Post

def showblog(request):#функция показать блог
	posts = Post.objects
	return render(request, 'blog/blog.html', {'posts': posts})

def specific_post(request, post_id):#функция отдельного поста
	post = get_object_or_404(Post, pk=post_id)#Post - класс, pk - основной ключ в базе данных
	return render(request, 'blog/specific_post.html', {'post':post})



# Create your views here.

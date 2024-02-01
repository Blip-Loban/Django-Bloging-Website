from typing import Any
from django.shortcuts import render,redirect
from .forms import *
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView,UpdateView, DeleteView,DetailView
from .models import Post
from django.utils.decorators import method_decorator
# Create your views here.
@login_required
def add_post(request):
    if request.method == 'POST':
        post_form = PostForm(request.POST, request.FILES)
        if post_form.is_valid():
            post = post_form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('homepage')
    else:
        post_form = PostForm()

    return render(request, 'add_post.html', {'form': post_form})

#Add Post using class based view
@method_decorator(login_required,name='dispatch')
class AddPostCreateView(CreateView):
    model=Post
    form_class= PostForm
    template_name='add_post.html'
    success_url= reverse_lazy('homepage')
    def form_valid(self, form):
        form.instance.author=self.request.user
        return super().form_valid(form)
    
#Add Update Post using class based view
@method_decorator(login_required,name='dispatch')   
class EditPostView(UpdateView):
    model = Post 
    form_class=PostForm
    template_name='add_post.html'
    pk_url_kwarg='id'
    success_url= reverse_lazy('homepage')

@method_decorator(login_required,name='dispatch')
class DeletePostView(DeleteView):
    model = Post 
    template_name='delete.html'
    pk_url_kwarg='id'
    success_url= reverse_lazy('homepage')





@login_required
def edit_post(request,id):
    post=Post.objects.get(pk=id)
    post_form=PostForm(instance=post)
    if request.method == 'POST':
        post_form=PostForm(request.POST, instance=post)
        if post_form.is_valid():
            post_form.instance.author=request.user
            post_form.save()
            return redirect('homepage')
 
    return render(request,'add_post.html',{'form':post_form})

@login_required
def delete_post(request, id):
    post=Post.objects.get(pk=id)
    post.delete()
    return redirect('homepage')



class DetailPostView(DetailView):
    model=Post
    pk_url_kwarg = 'id' 
    template_name='post_details.html'

    def post(self, request, *args, **kwargs):
        comment_form=CommentForm(data=self.request.POST)
        post=self.get_object()
        if comment_form.is_valid():
            new_comment=comment_form.save(commit=False)
            new_comment.post=post
            new_comment.save()
        return self.get(self, request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        post=self.object
        comments=post.comments.all()
        comment_form=CommentForm()
        context['comments']=comments
        context['comment_form']=comment_form
        return context

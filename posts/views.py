from django.shortcuts import render,redirect
from .forms import *
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from .models import *
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
class AddPostCreateView(CreateView):
    model=models.Post
    form_class=forms.PostForm
    template_name='add_post.html'
    success_url= reverse_lazy('homepage')
    def form_valid(self, form):
        form.instance.author=self.request.user
        return super().form_valid(form)
    




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


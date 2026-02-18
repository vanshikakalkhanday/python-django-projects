from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth.decorators import login_required

from django.contrib.admin.views.decorators import staff_member_required

from .models import Post , Comment

from .forms import PostForm, CommentForm

from django.core.paginator import Paginator
# READ - List all posts
def post_list(request):
   all_posts = Post.objects.all().order_by('-created_at')
   paginator = Paginator(all_posts, 3)      # 3 posts per page
   page_number = request.GET.get('page')
   posts = paginator.get_page(page_number)
   return render(request, 'blog/post_list.html', {'posts': posts})

# READ SINGLE POST

def post_detail(request, id):
   post = get_object_or_404(Post, id=id)
   comments = Comment.objects.filter(post=post)
   form = CommentForm(request.POST or None)
   if request.method == "POST":
       if form.is_valid():
           comment = form.save(commit=False)
           comment.post = post
           comment.save()
           return redirect('post_detail', id=post.id)
   return render(request, 'blog/post_detail.html', {
       'post': post,
       'comments': comments,
       'form': form
   })


# CREATE

def post_create(request):

    form = PostForm(request.POST or None)

    if form.is_valid():

        form.save()

        return redirect('post_list')

    return render(request, 'blog/post_form.html', {'form': form})

# UPDATE
@staff_member_required
def post_update(request, id):

    post = get_object_or_404(Post, id=id)

    form = PostForm(request.POST or None, instance=post)

    if form.is_valid():

        form.save()

        return redirect('post_list')

    return render(request, 'blog/post_form.html', {'form': form})

# DELETE
@staff_member_required
def post_delete(request, id):

    post = get_object_or_404(Post, id=id)

    post.delete()

    return redirect('post_list')
 
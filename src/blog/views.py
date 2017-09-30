from django.shortcuts import render, redirect, get_object_or_404
from django.utils.text import slugify
import markdown
from markdown.extensions.toc import TocExtension

from .models import Post
from .forms import PostCreateForm


def add_post_form(request):
    template_name = 'new_post.html'
    form = PostCreateForm(request.POST or None)
    context = {'form': form}
    if form.is_valid():
        post = form.save()
        return redirect('post/' + post.slug)
    if form.errors:
        context['errors'] = form.errors

    return render(request, template_name, context=context)


def index(request):
    return render(request, 'index.html', {'posts': Post.objects.all()})


def post_view(request, slug):
    post = get_object_or_404(Post, slug=slug)
    post.increase_views()

    md = markdown.Markdown(extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        'fenced_code',
        TocExtension(slugify=slugify)
    ])
    post.content = md.convert(post.content)

    context = {
        'banner': post.title,
        'subtitle': '目录',
        'category': md.toc,
        'post': post
    }

    return render(request, 'layout.html', context)

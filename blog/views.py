from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage,PageNotAnInteger
from .models import Post, Category


from django.db.models import Count
# You should change post in Count function based on your model.
categories = Category.objects.all().annotate(posts_count=Count('blog_posts'))
recent_posts = Post.published.all()

def post_list(request, category_slug=None):
    category = None
    posts = Post.published.all()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        posts = posts.filter(category=category)
    return render(request,
                 'blog/post/list.html',
                 {'category': category,
                  'categories': categories,
                  'posts': posts,
                  'recent_posts': recent_posts})

    object_list = Post.published.all()
    paginator = Paginator(object_list, 3) # 3 posts in each page
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)
    return render(request,
                  'blog/post/list.html',
                  {'category': category,
                  'categories': categories,
                  'page': page,
                  'posts': posts,
                  'recent_posts': recent_posts})
    

def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post,
                                   status='published',
                                   publish__year=year,
                                   publish__month=month,
                                   publish__day=day)
    return render(request, 'blog/post/detail.html',
                  {'post': post, 'recent_posts':recent_posts, 'categories': categories})

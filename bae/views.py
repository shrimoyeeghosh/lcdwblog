from django.shortcuts import render
from post.models import Post, Category, Tags
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Count, Q
from next_prev import next_in_order, prev_in_order


def post_by_category(request, name):
        #category = Category.objects.get(slug=category_slug)
        posts = Post.objects.filter(categories__title=name)
        paginator = Paginator(posts, 4)
        page_request_var = 'page'
        page = request.GET.get(page_request_var)
        try:
            paginated_queryset = paginator.page(page)
        except PageNotAnInteger:
            paginated_queryset = paginator.page(1)
        except EmptyPage:
            paginated_queryset = paginator.page(paginator.num_pages)
        context = {
            'posts': posts,
            'name': name,
            'page_request_var': page_request_var,
            'queryset': paginated_queryset
        }
        return render(request, 'category.html', context)


def post_by_tags(request, name):
    posts = Post.objects.filter(tags__title=name)
    paginator = Paginator(posts, 4)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)
    context = {
        'posts': posts,
        'name': name,
        'page_request_var': page_request_var,
        'queryset': paginated_queryset
    }
    return render(request, 'tags.html', context)


def search(request):
    queryset = Post.objects.all()
    query = request.GET.get('q')
    if query:
        queryset = queryset.filter(
            Q(title__icontains=query)
        ).distinct()
    context = {
    'queryset': queryset
    }
    return render(request, 'search_results.html', context)

def index(request):
    featured = Post.objects.filter(featured=True)[1:4]
    latest = Post.objects.order_by('-timestamp')[0:3]
    context = {
        'object_list': featured,
        'latest': latest
    }
    return render(request, 'index.html', context)


def get_category_count():
    queryset = Post.objects.values('categories__title').annotate(Count('categories__title'))
    print (queryset)
    return queryset


def blog(request):
    category_count = get_category_count()
    most_recent = Post.objects.order_by('-timestamp')[:3]
    post_list= Post.objects.all()
    paginator = Paginator(post_list, 4)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)
    context = {
        'queryset': paginated_queryset,
        'most_recent': most_recent,
        'page_request_var': page_request_var,
        'category_count': category_count
    }
    return render(request, 'blog.html', context)

def post(request, id):
    post = Post.objects.get(id=id)
    categ = Category.objects.all
    category_count = get_category_count()
    most_recent = Post.objects.order_by('-timestamp')[:3]
    context = {
    'post': post,
    'most_recent': most_recent,
    'category_count': category_count,
    'categ': categ
    }
    return render(request, 'post.html', context)

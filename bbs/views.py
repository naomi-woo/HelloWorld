from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import User, Post, Comment, Category
from .forms import CommentForm

# Create your views here.
# 회원가입 페이지
def signup(request):
    return render(
        request, 
        'bbs/signup.html'
    )

# 로그인 페이지
def login(request):
    return render(
        request,
        'bbs/login.html'
    )

# 게시글 조회 페이지
class PostDetail(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super(PostDetail,self).get_context_data()
        context['categories'] = Category.objects.all()
        context['no_category_post_count'] = Post.objects.filter(category=None).count
        context['comment_form'] = CommentForm
        return context
    # 템플릿은 모델명_detail.html : post_detail.html
    # 매개변수 모델명 : post

# 게시글 작성 페이지
class PostCreate(CreateView):
    model = Post
    fields = ['title', 'category', 'content', 'file']

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PostCreate,self).get_context_data()
        context['categories'] = Category.objects.all()
        context['no_category_post_count'] = Post.objects.filter(category=None).count
        return context
    # 모델명_form.html

# 대문 페이지, 카테고리 별 최신 Post 목록 출력 페이지
class PostList(ListView):
    model = Post
    ordering = '-pk'
    paginate_by = 3

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PostList,self).get_context_data()
        context['categories'] = Category.objects.all()
        context['no_category_post_count'] = Post.objects.filter(category=None).count
        return context
    # 템플릿은 모델명_list.html : post_list.html
    # 매개변수 모델명_list : post_list



# 카테고리별 Post 목록 출력 페이지
def category_list(request, slug):
    if slug == 'no_category':
        category = '미분류'
    else :
        category = Category.objects.get(slug=slug)
    return render(request, 'blog/category_list.html', {
        'category' : category,
        'categories' : Category.objects.all(),
        'no_category_post_count' : Post.objects.filter(category=None).count,
    })
    
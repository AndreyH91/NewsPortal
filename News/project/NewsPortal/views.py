from django.views.generic import ListView, DetailView
from .models import Post


class PostList(ListView):
    model = Post                        # указываем модель, объекты которой мы будем выводить
    template_name = 'news/posts.html'   # указываем имя шаблона, в котором будет лежать HTML, в котором будут все инструкции о том, как именно пользователю должны вывестись наши объекты
    context_object_name = 'posts'       # это имя списка, в котором будут лежать все объекты, его надо указать, чтобы обратиться к самому списку объектов через HTML-шаблон
    queryset = Post.objects.order_by('-dateCreation')



class PostDetail(DetailView):
    model = Post                        # модель чьи объекты выводятся
    template_name = 'news/post.html'    # путь и название шаблона html
    context_object_name = 'post'
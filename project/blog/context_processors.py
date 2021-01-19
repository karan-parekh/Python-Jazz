from django.contrib.auth.models import User
from .models import Post



def info_processor(request):

    users_count = User.objects.count
    posts_count = Post.objects.count
    your_posts = 0

    user = request.user

    if user.is_authenticated:

        posts = Post.objects.filter(author=user)

        your_posts = posts.count

    return {
        'total_users': users_count,
        'total_posts': posts_count,
        'your_posts' : your_posts
    }

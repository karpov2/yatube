from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse('Welcome')


def group_posts(request, group):
    return HttpResponse(f'group_posts {group}')

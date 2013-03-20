from post.models import Tags, Category

def navigation(request):
    return {'all_categories': Category.objects.all(), 'all_tags': Tags.objects.all()}

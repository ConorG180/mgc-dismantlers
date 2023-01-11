from products.models import Category


def category_context_processor(request):
    categories = Category.objects.all()
    return {'categories': categories}

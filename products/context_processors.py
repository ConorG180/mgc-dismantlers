from products.models import Category, Make, Model, Part


def category_context_processor(request):
    categories = Category.objects.all()
    makes = Make.objects.all()
    car_models = Model.objects.all()
    parts = Part.objects.all()
    years = range(1950, 2024)
    return {
        'categories': categories,
        'makes': makes,
        'car_models': car_models,
        'parts': parts,
        'years': years,
    }

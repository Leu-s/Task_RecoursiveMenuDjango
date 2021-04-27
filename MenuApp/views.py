from django.shortcuts import render
from .models import Category


def index(request):
    template = 'index.html'
    categories = Category.objects.all()
    return render(request=request, context={'categories': categories}, template_name=template)


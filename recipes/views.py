from django.shortcuts import render

from recipes.models import Author, Recipe


def index_view(request):
    my_recipes = Recipe.objects.all()
    return render(request, 'index.html', {"recipes": my_recipes, "page_title": "Recipe Box"})


def author_detail_view(request, author_id):
    my_author = Author.objects.filter(id=author_id)
    return render(request, 'author_detail.html', {"author": my_author})


def recipe_detail_view(request, recipe_id):
    my_recipe = Recipe.objects.filter(id=recipe_id)
    return render(request, 'recipe_detail.html', {"recipe": my_recipe})

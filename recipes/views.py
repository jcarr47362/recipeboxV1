from django.shortcuts import render

from recipes.models import Author, Recipe
from .forms import AddAuthorForm, AddRecipeForm


def index_view(request):
    my_recipes = Recipe.objects.all()
    return render(request, 'index.html', {"recipes": my_recipes, "page_title": "Recipe Box"})


def author_detail_view(request, author_id):
    my_author = Author.objects.filter(id=author_id).first()
    author_recipes = Recipe.objects.filter(author=my_author)
    return render(request, 'author_detail.html', {"author": my_author, "recipes": author_recipes})


def recipe_detail_view(request, recipe_id):
    my_recipe = Recipe.objects.filter(id=recipe_id).first()
    return render(request, 'recipe_detail.html', {"recipe": my_recipe})


def add_author(request):
    form = AddAuthorForm()
    return render(request, "add_author.html", {"author_form": form})


def add_recipe(request):
    if request.method == "POST":
        form = AddRecipeForm(request.POST)
    form = AddRecipeForm()
    return render(request, "add_recipe.html", {"recipe_form": form})

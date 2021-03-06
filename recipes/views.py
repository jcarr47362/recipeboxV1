from django.shortcuts import render, HttpResponseRedirect, reverse

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
    if request.method == "POST":
        form = AddAuthorForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Author.objects.create(
                name=data.get('name'),
                bio=data.get('bio')
            )
            return HttpResponseRedirect(reverse("recipes"))

    form = AddAuthorForm()
    return render(request, "add_author.html", {"author_form": form})


def add_recipe(request):
    if request.method == "POST":
        form = AddRecipeForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Recipe.objects.create(
                title=data.get('title'),
                author=data.get('author'),
                description=data.get('description'),
                time_required=data.get('time_required'),
                instructions=data.get('instructions')
            )
            return HttpResponseRedirect(reverse("recipes"))

    form = AddRecipeForm()
    return render(request, "add_recipe.html", {"recipe_form": form})

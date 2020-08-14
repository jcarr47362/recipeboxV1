from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User

from recipes.models import Author, Recipe
from .forms import AddAuthorForm, AddRecipeForm, LoginForm, SignupForm


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


@login_required
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

    messages.add_message(request, messages.INFO,
                         'You permission-level doesn\'t allow access')
    form = AddAuthorForm()
    return render(request, "add_author.html", {"author_form": form})


@login_required
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


def login_view(request):

    valuenext = request.POST.get('next')

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data.get(
                "username"), password=data.get("password"))
            if user:
                login(request, user)
                return HttpResponseRedirect(request.GET.get('next'), reverse("recipes"))

    form = LoginForm()
    return render(request, "login.html", {"form": form})


def signup_view(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_user = User.objects.create_user(username=data.get(
                "username"), password=data.get("password"))
            login(request, new_user)
            return HttpResponseRedirect(reverse("recipes"))

    form = SignupForm()
    return render(request, "signup.html", {"form": form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("recipes"))

from django import forms
from recipes.models import Author, Recipe


class AddAuthorForm(forms.Form):
    name = forms.CharField(label='Name', max_length=50)
    bio = forms.CharField(widget=forms.Textarea)


class AddRecipeForm(forms.Form):
    title = forms.CharField(max_length=50)
    description = forms.CharField(widget=forms.Textarea())
    instructions = forms.CharField(widget=forms.Textarea)
    time_required = forms.CharField(max_length=80)
    author = forms.ModelChoiceField(queryset=Author.objects.all())


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ["name"]

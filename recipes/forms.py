from django import forms


class AddAuthorForm(forms.Form):
    name = forms.CharField(label='Name', max_length=50)
    bio = forms.CharField(widget=forms.Textarea)


class AddRecipeForm(forms.Form):
    title = forms.CharField(max_length=50)
    author = ''
    description = forms.CharField(widget=forms.Textarea())

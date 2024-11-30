from django import forms
from .models import Post, Author
from django_filters import ModelChoiceFilter

class PostForm(forms.ModelForm):
    author = ModelChoiceFilter(
        queryset=Author.objects.all(),  # Получение всех авторов из базы
        empty_label='Все авторы',  # Опция выбора "Все авторы"
        required=False  # Делаем это поле необязательным
    )

    class Meta:
        model = Post
        fields = [
            'title',
            'text',
            'postCategory',
            'author'
        ]
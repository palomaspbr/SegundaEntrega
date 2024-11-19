from django.forms import ModelForm
from .models import Post, Review


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = [
            'name',
            'description',
            'poster_url',
        ]
        labels = {
            'name': 'Título',
            'description': 'Descrição',
            'poster_url': 'URL da Imagem do Post',
        }

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = [
            'author',
            'text',
        ]
        labels = {
            'author': 'Usuário',
            'text': 'Comentário',
        }
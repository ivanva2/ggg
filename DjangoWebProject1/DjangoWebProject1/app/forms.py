"""
Definition of forms.
"""
from .models import Blog
from django.db import models
from .models import Comment
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _

class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=_("Пароль"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))
class otzivform(forms.Form):
    name=forms.CharField(label='Ваше имя', min_length=2, max_length=100)
    city=forms.CharField(label='Ваш город', min_length=2, max_length=100)
    purchases=forms.BooleanField(label='Совершали покупки?',
                                 required=False)
    grade=forms.ChoiceField(label="Оцените удобство сайта от 1 до 5",
                            choices=(('1','1'),
                                     ('2','2'),
                                     ('3','3'),
                                     ('4','4'),
                                     ('5','5')),initial=1)
    message=forms.CharField(label='Отзыв',
                            widget=forms.Textarea(attrs={'rows':12,'cols':20}))
class CommentForm (forms.ModelForm):

    class Meta:
        
        model = Comment # используемая модель

        fields = ('text',) # требуется заполнить только поле text

        labels = {'text': "Комментарий"} # метка к полю формы text
class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = {'title', 'description', 'content','image',}
        labels = {'title': "Заголовок",'description':"Краткое содержание",'content':"Полное содержание",'image':"Картинка"}

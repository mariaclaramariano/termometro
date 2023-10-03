
from django import forms

class FeedbackForm(forms.Form):
    email = forms.EmailField(label='Seu email:')
    emoji_choices = (
        ('😆', '😆'),
        ('😃', '😃'),
        ('😊',  '😊'),
        ('😐', '😐'),
        ('😥','😥'),
        ('😞', '😞'),
        ('😫','😫'),
    )

    
    emoji = forms.ChoiceField(label='Escolha um Emoji:', choices=emoji_choices, widget=forms.RadioSelect)

    comentario = forms.CharField(label='Faça um comentário:', widget=forms.Textarea(attrs={'rows': 5, 'cols': 50}))
 
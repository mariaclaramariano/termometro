from django.shortcuts import render
from .forms import FeedbackForm

def feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            emoji = form.cleaned_data['emoji']
            comentario = form.cleaned_data['comentario']
        return render(request, 'feedback.html', { 'form': form})
            
    else:
        form = FeedbackForm()
    
    return render(request, 'feedback.html', {'form': form})

from django.shortcuts import render

# Create your views here.
def index(request):
    """Strona główna aplikacji Learning Log."""
    return render(request, 'learning_logs/index.html')
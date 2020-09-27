from django.shortcuts import render

from .models import Topic

# Create your views here.
def index(request):
    """Strona główna aplikacji Learning Log."""
    return render(request, 'learning_logs/index.html')

def topics(request):
    """Wyświetlenie wszystkich tematów"""
    topics = Topic.objects.order_by('data_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)

def topic(request, topic_id):
    """Wyświetla pojedyńczy temat i wszystkie powiązane z nim wpisy."""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)

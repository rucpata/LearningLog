from django.shortcuts import render
from django.http import HttpResponseRedirect #Przekierowanie uzytkownika po dodaniu nowego tematu do strony topic
from django.core.urlresolvers import reverse 

from .models import Topic
from .models import TopicForm

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

def new_topic(request):
    """Dodaj nowy temat"""
    if request.method != 'POST':
        #Nie przekazano zadnych danych nalezy utowrzyc pusty formularz
        form = TopicForm()
    else:
        #Przekazano dane za pomoca zadania POST, nalezy je przetworzyc
        form = TopicForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('topcs'))

        context = {'form': form}
        return render(request, 'new_topic.html', context)
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect #Przekierowanie uzytkownika po dodaniu nowego tematu do strony topic
from django.urls import reverse 

from .models import Topic
from .forms import TopicForm, EntryForm



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
    """Dodanie nowego tematu"""
    if request.method != 'POST':
        #Nie przekazano zadnych danych, nalezy utworzyc pusty formularz
        form = TopicForm()
    else:
        #Przekazano dane za pomocą zadania POST, nalezy je przetowrzyc
        form = TopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('topics')
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)

def new_entry(request, topic_id):
    """Dodanie nowego wpisu dla określonego tematu."""
    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        #Nie przekazano zadnych danych, nalezy utworzyc pusty formularz
        form = EntryForm()
    else: 
        #Przekazano dane za pomocą zadania POST, nalezy je przetowrzyc
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('topic', topic_id=topic_id)
        
    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)
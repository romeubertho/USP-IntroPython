from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import Topic, Entry
from .forms import TopicForm, EntryForm
# tentando enviar em Json!
from django.http import JsonResponse

# Create your views here.


def index(request):
    """Home page"""
    return render(request, 'index.html')
# testeeeeee


def teste(request):
    """Testeeeeeee"""
    return render(request, 'teste.html')
# topics


def topics(request):
    """Topics"""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'topics.html', context)


# topic
def topic(request, topic_id):
    """Topic"""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {
        'topic': topic,
        'entries': entries
    }
    return render(request, 'topic.html', context)


# getTopic
def getTopic(request, topic_id):
    """getTopic"""
    topic = Topic.objects.get(id=topic_id)
    topic_list = list(topic)
    # return render(request,context)
    return JsonResponse(topic_list, safe=False)

# Adicionar um novo topico


def new_topic(request):
    if request.method != 'POST':
        # No data submitted; create a blank form
        form = TopicForm()
    else:
        # POST
        form = TopicForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learning_logs:topics'))
    context = {
        'form': form
    }
    return render(request, 'new_topic.html', context)

# Nova entrada


def new_entry(request, topic_id):
    """Add a new entry for a particular topic."""
    topic = Topic.objects.get(id=topic_id)
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = EntryForm()
    else:
        # POST data submitted; process data.
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse('learning_logs:topic', args=[topic_id]))

    context = {'topic': topic, 'form': form}
    return render(request, 'new_entry.html', context)

# Editar entrada


def edit_entry(request, entry_id):
    """Edit an existing entry."""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    if request.method != 'POST':
        # Initial request; pre-fill form with the current entry.
        form = EntryForm(instance=entry)
    else:
        # POST data submitted; process data.
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learning_logs:topic', args=[topic.id]))

    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'edit_entry.html', context)

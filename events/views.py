from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from . import forms
from .models import Event


# Create your views here.

@login_required()
def events_list(request):
    # events = Event.objects.all().order_by('date')
    events = Event.objects.filter(is_archive=False).order_by('date')
    return render(request, 'events/events_list.html', {'events': events})


@login_required()
def archived_list(request):
    events = Event.objects.filter(is_archive=True)
    return render(request, 'events/archived_list.html', {'events': events})


@login_required()
def event_details(request, id):
    event = Event.objects.get(id=id)
    return render(request, 'events/event_details.html', {'event': event})


@login_required()
def add_event(request):
    if request.method == 'POST':
        form = forms.AddEvent(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.posted_by = request.user
            instance.save()
            return redirect('events:events_list')
    form = forms.AddEvent()
    return render(request, 'events/add_event.html', {'form': form})


@login_required()
def edit_event(request, id):
    instance = get_object_or_404(Event, id=id)
    form = forms.AddEvent(request.POST or None, instance=instance)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('events:events_list')

    return render(request, 'events/edit_event.html', {'form': form, 'event': instance})


@login_required()
def archive_event(request, id):
    event = Event.objects.get(id=id)
    event.is_archive = True
    event.save()
    return redirect('events:archived_list')


@login_required()
def delete_event(request, slug):
    event = Event.objects.get(slug=slug)
    event.delete()
    return redirect('events:events_list')


@login_required()
def search_event(request):
    if request.method == 'POST':
        search = request.POST.get('search')
        events = Event.objects.filter(title=search)
        if events:
            return render(request, 'events/event_details.html', {'event': events[0]})
        else:
            return redirect('events:events_list')
    else:
        return redirect('events:events_list')

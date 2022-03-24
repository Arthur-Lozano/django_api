from django.shortcuts import render
from .models import Note
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

class NoteListView(ListView):
    template_name = 'note-list.html'
    model = Note
    context_object_name = 'note_list'

class NoteDetailView(DetailView):
    template_name = 'note-detail.html'
    model = Note

class NoteCreateView(CreateView):
    template_name = 'note-create.html'
    model = Note
    fields = ['title', 'category', 'description']
    success_url = reverse_lazy('note_list')

class NoteUpdateView(UpdateView):
    template_name = 'note-update.html'
    model = Note
    fields = ['title',  'category', 'description']

class NoteDeleteView(DeleteView):
    template_name = 'note-delete.html'
    model = Note
    success_url = reverse_lazy('note_list')

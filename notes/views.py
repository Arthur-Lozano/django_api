from django.shortcuts import render
from .models import Note
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from .serializer import NoteSerializer



class NoteListView(generics.ListCreateAPIView):
    # template_name = 'note-list.html'
    # model = Note
    # context_object_name = 'note_list'
    permission_classes = (IsAuthenticated,)
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

class NoteDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    # template_name = 'note-detail.html'
    # model = Note

class NoteCreateView(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    # template_name = 'note-create.html'
    # model = Note
    # fields = ['title', 'category', 'description']
    # success_url = reverse_lazy('note_list')

class NoteUpdateView(generics.UpdateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    # template_name = 'note-update.html'
    # model = Note
    # fields = ['title',  'category', 'description']

class NoteDeleteView(generics.DestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Note.objects.all()
    serializer_class = NoteSerializer             
    # template_name = 'note-delete.html'
    # model = Note
    # success_url = reverse_lazy('note_list')

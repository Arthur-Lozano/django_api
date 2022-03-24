from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

class Note(models.Model):
    title= models.CharField(max_length=64)
    category = models.CharField(max_length=64, null=True, blank=True)
    description = models.TextField(default='')
    createdAt = models.DateTimeField(auto_now_add=True)
    # purchaser = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('note_detail', args=[str(self.id)])

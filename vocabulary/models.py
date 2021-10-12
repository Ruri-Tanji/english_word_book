from django.db import models
from accounts.models import User


class VocabularyCategory(models.Model):
    name = models.CharField(max_length=100)
    
    
class Vocabulary(models.Model):
    name = models.CharField(max_length=100)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(VocabularyCategory, on_delete=models.DO_NOTHING)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='vocabulary')
    favorites = models.ManyToManyField(User, related_name='favorites')

    def __str__(self):
        return self.name


class Word(models.Model):
    noun = models.CharField(max_length=100)
    explain = models.TextField()
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    vocabulary = models.ForeignKey(Vocabulary, on_delete=models.CASCADE, related_name='words')
    
    def __str__(self):
        return self.noun

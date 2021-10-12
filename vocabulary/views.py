from django.shortcuts import render, redirect
from .models import Vocabulary, Word, VocabularyCategory
from django.views.generic import View


def top(request):
    vocabs = Vocabulary.objects.filter(id__lte=3)
    categories = VocabularyCategory.objects.all()
    context = {
        'vocabs': vocabs,
        'categories': categories
        }
    return render(request, 'vocabulary/top.html', context)


def index(request):
    vocabs = Vocabulary.objects.all()
    context = {'vocabs': vocabs}
    return render(request, 'vocabulary/index.html', context)


def detail(request, vocab_id):
    vocab = Vocabulary.objects.get(pk=vocab_id)
    context = {'vocab': vocab}
    return render(request, 'vocabulary/detail.html', context)


def create(request):
    if request.POST:
        vocabulary = Vocabulary.objects.create(
            name=request.POST.get('name'),
            category=VocabularyCategory.objects.get(pk=request.POST.get('category')),
            author=request.POST.get('username')
        )
        return redirect('detail', vocabulary.id)
    categories = VocabularyCategory.objects.all()
    context = {
        "categories": categories
    }
    return render(request, 'vocabulary/create.html', context)

def about(request):
    return render(request, 'vocabulary/about.html')


# def edit(request, vocab_id):
#     vocab = Vocabulary.objects.get(pk=vocab_id)
#     category = VocabularyCategory.objects.get(pk=vocab.category)
#     if request.POST:
#             vocab.name = request.POST.get('name')
#         vocab.category = request.POST.get('category')
#         word = Word.objects.create(
#             noun=request.POST.get('noun'),
#             explain=request.POST.get('explain'),
#             author=request.POST.get('username'),
#             vocabulary=Vocabulary.objects.get(pk=vocab_id)
#         )
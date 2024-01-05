# sampleapp/views.py
from django.shortcuts import render
from .models import Collection, Sample

def collection_list(request):
    collections = Collection.objects.all()
    return render(request, 'collection_list.html', {'collections': collections})

def collection_detail(request, collection_id):
    collection = Collection.objects.get(id=collection_id)
    samples = Sample.objects.filter(collection_id=collection_id)
    return render(request, 'collection_detail.html', {'collection': collection, 'samples': samples})

# Implement other views for adding samples, creating collections, etc.


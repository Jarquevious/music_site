from django.http import HttpResponse
from django.shortcuts import render
from .models import * 

def list_page(request):
  context = {
    'musician': Musician.objects.all()
  }
  return render(request, 'list_page.html', context)

# def detail(request, book_id):
#     context = {
#         'musician': Book.objects.get(id=book_id)
#     }
#     return render(request, 'detail.html', context)

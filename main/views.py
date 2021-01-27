from django.shortcuts import render
from django.http import HttpResponse
from .models import QuranReg
from .forms import MyForm, MyForm2, MyForm3

# Create your views here.
def home(request):
	return render(request, 'main/home.html')
def egazat(request):
	return render(request, 'main/egazat.html')
def quran(request):
	return render(request, 'main/quran.html')
def tajweed(request):
	return render(request, 'main/tajweed.html')
def about(request):
  return render(request, 'main/about.html')

def register_q(request):
  if request.method == "POST":
    form = MyForm(request.POST)
    if form.is_valid():
      form.save()
  else:
      form = MyForm()
  return render(request, 'main/register_q.html', {'form': form})

def register_e(request):
  if request.method == "POST":
    form = MyForm3(request.POST)
    if form.is_valid():
      form.save()
  else:
      form = MyForm3()
  return render(request, 'main/register_e.html', {'form': form})

def register_t(request):
  if request.method == "POST":
    form = MyForm2(request.POST)
    if form.is_valid():
      form.save()
  else:
      form = MyForm2()
  return render(request, 'main/register_t.html', {'form': form})

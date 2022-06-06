from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404
from .models import Memory
from .forms import MemoryForm

def login(request):
    """"Страница для входа"""
    return render(request, 'memories/login.html')

def index(request):
    """"Домашняя страница приложения Memory"""
    try:
        memories = Memory.objects.filter(owner=request.user)
        context = {'memories': memories}
        return render(request, 'memories/index.html', context)
    except:
        return render(request, 'memories/index.html')

@login_required
def new_memory(request):
    """"Определяет новое воспоминание"""
    if request.method != 'POST':
        form = MemoryForm()
    else:
        """"Обрабатываем данные POST"""
        form = MemoryForm(request.POST)
        if form.is_valid():
            new_memory = form.save(commit=False)
            new_memory.owner = request.user
            new_memory.save()
            return redirect('memories:index')

    # Вывести пустую или недействительную форму
    context = {'form': form}
    return render(request, 'memories/new_memory.html', context)

@login_required
def memory(request, memory_id):
    """"Редактирует воспоминание"""
    memory = Memory.objects.get(id=memory_id)
    if memory.owner != request.user:
        raise Http404

    if request.method != 'POST':
        form = MemoryForm(instance=memory)
    else:
        form = MemoryForm(request.POST, instance=memory)
        if form.is_valid():
            form.save()
            return redirect('memories:index')

    context = {'memory': memory, 'form': form}
    return render(request, 'memories/memory.html', context)
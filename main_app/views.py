from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView
from .models import Computer, Comment, Peripheral
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm



# Create your views here.
def home(request):
    return render(request, 'home.html')

# this is cat_index route
def community(request):
    computers = Computer.objects.all().order_by('id')
    return render(request, 'computers/community.html', {"computers": computers})

def computer_detail(request, computer_id):
    computer = get_object_or_404(Computer, id=computer_id)
    comments = Comment.objects.filter(computer=computer)
    peripherals = Peripheral.objects.filter(computer=computer)

    context = {
        'computer': computer,
        'comments': comments,
        'peripherals': peripherals,
    }
    return render(request, 'computers/detail.html', context)

class ComputerCreate(LoginRequiredMixin, CreateView):
    model = Computer
    fields = ['name', 'comptype', 'cpu', 'gpu', 'ram']

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class ComputerUpdate(LoginRequiredMixin, UpdateView):
    model = Computer
    fields = ['name', 'comptype', 'cpu', 'gpu', 'ram']

class ComputerDelete(LoginRequiredMixin, DeleteView):
    model = Computer
    success_url = reverse_lazy('community')

class CommentCreate(LoginRequiredMixin, CreateView):
    model = Comment
    fields = ['text']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        pk = self.kwargs['pk']
        computer = Computer.objects.get(id=pk)
        form.instance.computer = computer
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('computer-detail', kwargs={'computer_id': self.kwargs['pk']})

class CommentUpdate(LoginRequiredMixin, UpdateView):
    model = Comment
    fields = ['text']

    def get_object(self, queryset=None):
        computer_id = self.kwargs['computer_id']
        comment_id = self.kwargs['comment_id']
        return Comment.objects.get(id=comment_id, computer_id=computer_id)

    
    def get_success_url(self):
        return reverse_lazy('computer-detail', kwargs={'computer_id': self.kwargs['computer_id']})

class CommentDelete(LoginRequiredMixin, DeleteView):
    model = Comment

    def get_object(self, queryset=None):
        computer_id = self.kwargs['computer_id']
        comment_id = self.kwargs['comment_id']
        return Comment.objects.get(id=comment_id, computer_id=computer_id)

    
    def get_success_url(self):
        computer_id = self.kwargs['computer_id']
        return reverse_lazy('computer-detail', kwargs={'computer_id': computer_id})

class PeripheralsCreate(LoginRequiredMixin, CreateView):
    model = Peripheral
    fields = ['keyboard', 'mouse', 'monitor1', 'monitor2', 'monitor3']

    def form_valid(self, form):
        computer_id = self.kwargs['computer_id']
        computer = get_object_or_404(Computer, id=computer_id)
        form.instance.computer = computer
        return super().form_valid(form)
    
    def get_success_url(self):
        computer_id = self.kwargs['computer_id']
        return reverse_lazy('computer-detail', kwargs={'computer_id': computer_id})

class PeripheralsUpdate(LoginRequiredMixin, UpdateView):
    model = Peripheral
    fields = ['keyboard', 'mouse', 'monitor1', 'monitor2', 'monitor3']

    def get_object(self, queryset=None):
        computer_id = self.kwargs.get('pk')
        peripheral = get_object_or_404(Peripheral, computer__id=computer_id)
        return peripheral
    
    def get_success_url(self):
        computer_id = self.kwargs.get('pk')
        return reverse_lazy('computer-detail', kwargs={'computer_id': computer_id})

class PeripheralsDelete(LoginRequiredMixin, DeleteView):
    model = Peripheral

    def get_success_url(self):
        computer_id = self.kwargs.get('pk')
        return reverse_lazy('computer-detail', kwargs={'computer_id': computer_id})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        computer_id = self.kwargs.get('pk')
        computer = get_object_or_404(Computer, id=computer_id)
        context['computer'] = computer
        return context

    def get_object(self, queryset=None):
        computer_id = self.kwargs.get('pk')
        peripheral = get_object_or_404(Peripheral, computer__id=computer_id)
        return peripheral
    
class Home(LoginView):
    template_name = 'home.html'
        
def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('community')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)

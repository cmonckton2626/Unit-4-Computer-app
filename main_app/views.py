from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.views.generic import CreateView, UpdateView, DeleteView
from .models import Computer, Comment
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
def home(request):
    return render(request, 'home.html')

# this is cat_index route
def community(request):
    computers = Computer.objects.all()
    return render(request, 'computers/community.html', {"computers": computers})

def computer_detail(request, computer_id):
    computer = get_object_or_404(Computer, id=computer_id)
    comments = Comment.objects.filter(computer=computer)
    return render(request, 'computers/detail.html', {'computer': computer, 'comments': comments})

class ComputerCreate(LoginRequiredMixin, CreateView):
    model = Computer
    fields = "__all__"

class ComputerUpdate(LoginRequiredMixin, UpdateView):
    model = Computer
    fields = '__all__'

class ComputerDelete(LoginRequiredMixin, DeleteView):
    model = Computer
    success_url = '/community/'

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








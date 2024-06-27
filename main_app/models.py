from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Computer(models.Model):
    COMPUTER_TYPE_CHOICES = [
        ('desktop', 'Desktop'),
        ('laptop', 'Laptop'),
        ('tablet', 'Tablet'),
        ('all-in-one', 'All-in-One PC'),
        ('other', 'Other'),
    ] 
    
    name = models.CharField(max_length=100, verbose_name="Computer Name")
    comptype = models.CharField(max_length=20, choices=COMPUTER_TYPE_CHOICES, verbose_name="Computer Type", blank=True)
    cpu = models.CharField(max_length=100, verbose_name="CPU", blank=True)
    gpu = models.CharField(max_length=100, verbose_name="GPU", blank=True)
    ram = models.CharField(max_length=100, verbose_name="RAM", blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='computer')
    # pic = # i dont know how to do this yet

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('computer-detail', kwargs={'computer_id': self.id})

class Comment(models.Model):
    text = models.TextField(max_length=500)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    computer = models.ForeignKey(Computer, on_delete=models.CASCADE, related_name='comments', null=False, blank=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.author.username}: {self.text[:20]}'
    
    class Meta:
        ordering = ['-timestamp']

class Peripheral(models.Model):
    keyboard = models.CharField(max_length=100, verbose_name="Keyboard", blank=True)
    mouse = models.CharField(max_length=100, verbose_name="Mouse", blank=True)
    monitor1 = models.CharField(max_length=100, verbose_name="Monitor 1")
    monitor2 = models.CharField(max_length=100, verbose_name="Monitor 2", blank=True)
    monitor3 = models.CharField(max_length=100, verbose_name="Monitor 3", blank=True)
    computer = models.OneToOneField(Computer, on_delete=models.CASCADE, related_name='peripherals')
    # pic = # i dont know how to do this yet

    def __str__(self):
        return f"Peripherals for {self.computer.owner.username}'s computer"

    def get_absolute_url(self):
        return reverse('computer-peripherals', kwargs={'computer_id': self.computer.id})
    






from django.shortcuts import render
from .models import Subjects
from django.utils import timezone

def post_list(request):
    sub = Subjects.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request,'firstapp/post_list.html',{'sub':sub})
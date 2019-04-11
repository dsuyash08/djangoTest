from django.shortcuts import render, get_object_or_404
from .models import Subjects
from django.utils import timezone

def post_list(request):
    sub = Subjects.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request,'firstapp/post_list.html',{'sub':sub})

def subjects_detail(request,pk):
    sub = get_object_or_404(Subjects,pk=pk)
    return render(request, 'firstapp/subjects_detail.html', {'sub':sub})
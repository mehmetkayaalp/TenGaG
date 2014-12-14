from django.shortcuts import render
from tenGag.models import CommentInfo
from tenGag.models import Gag
from tenGag.forms import CommentForm
from tenGag.forms import GagForm

def show_comment(request):
    form = CommentForm()
    if request.POST:
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()

    comments = CommentInfo.objects.all()
    return render(request, 'commentPage.html', {'form': form, 'comments': comments})

def add_gag(request):
    form = GagForm()
    if request.POST:
        form = GagForm(request.POST)
        if form.is_valid():
            form.save()

    gags = Gag.objects.all()
    print "entered add_gag"
    return render(request, 'commentPage.html', {'form': form, 'gags': gags})

#def count_votes(request):
#    comment_number = CommentInfo.objects.count()

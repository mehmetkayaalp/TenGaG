from django.shortcuts import render
from tenGag.models import CommentInfo
from tenGag.forms import CommentForm


def show_comment(request):
    form = CommentForm()
    if request.POST:
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()

    comments = CommentInfo.objects.all()
    return render(request, 'commentPage.html', {'form': form, 'comments': comments})


#def count_votes(request):
#    comment_number = CommentInfo.objects.count()

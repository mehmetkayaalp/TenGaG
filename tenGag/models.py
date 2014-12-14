from django.db import models


class CommentInfo (models.Model):

    commentContent = models.TextField(max_length=200)
#   date = models.DateField(auto_now_add=True)

# class Vote (models.Model):
#    comment = models.ForeignKey(CommentInfo)


class LikeInfo (models.Model):
    created_time = models.DateField(auto_now_add=True)
    created_comment = models.ForeignKey(CommentInfo)
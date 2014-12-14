from django.db import models


class Gag (models.Model):
    title = models.TextField(max_length=20)
    image = models.ImageField(upload_to='gag', null=True)

    def __unicode__(self):
        return u'title: %s, image: %s' % (self.title,self.image)

class CommentInfo (models.Model):

    commentContent = models.TextField(max_length=200)
    gag = models.ForeignKey(Gag, null=True)

#   date = models.DateField(auto_now_add=True, null=True)

# class Vote (models.Model):
#    comment = models.ForeignKey(CommentInfo)


class LikeInfo (models.Model):
    created_time = models.DateField(auto_now_add=True)
    created_comment = models.ForeignKey(CommentInfo)
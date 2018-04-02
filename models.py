from django.db import models

# Create your models here.
class Proposal(models.Model):
    text = models.CharField(max_length = 99999)
    parent = models.IntegerField(default=-1)
    voteC = models.IntegerField(default=0)
    voteI = models.IntegerField(default=0)
    voteL = models.IntegerField(default=0)
    children = models.CharField(default = '',max_length = 9999999)

    def get_children(self):
        childlist = []
        for i in self.children.split(','):
            childlist.append(int(i))
        return childlist

    def set_children(self,childlist):
        self.children = ''
        for i in childlist:
            self.children += str(i)+','
        self.children = self.children[:-1]

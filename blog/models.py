from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
        

def json_default_post(self):
    domain = 'https://python.web.id'
    cover_url = 'None'
    try:
        cover_url = domain+str(self.cover.url)
    except:
        cover_url = cover_url

    return dict(
            title = self.title, 
            url = domain+"/blog/"+str(self.slug), 
            cover =  cover_url,
            author = self.author.name, 
            created = self.created.isoformat(), 
            modified = self.modified.isoformat(), 
            tags = [p.slug for p in self.tags.all()], 
            body = self.body
        )
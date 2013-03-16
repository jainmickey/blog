from django.db import models

# Create your models here.

class Tags(models.Model):
    tag = models.CharField(max_length=50)
    
    def get_posts(self):
        return self.post_set.all()

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

    def __unicode__(self):
        return self.tag

class Category(models.Model):
    category = models.CharField(max_length=100)

    def get_posts(self):
        return self.post_set.all()

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __unicode__(self):
        return self.category

class Post(models.Model):
    title = models.CharField(max_length=300)
    body = models.TextField()
    date = models.DateField(auto_now=True)
    tags = models.ManyToManyField(Tags)
    category = models.ForeignKey(Category)

    def get_tags(self):
        return self.tags.all()

    def __unicode__(self):
        return self.title

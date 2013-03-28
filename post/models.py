from django.contrib.auth.models import User
from django.db import models
from django.template.defaultfilters import slugify
from django.core.urlresolvers import reverse

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
    date = models.DateTimeField(auto_now=True, editable=False)
    published = models.BooleanField(default=True)
    tags = models.ManyToManyField(Tags)
    category = models.ForeignKey(Category)
    author = models.ForeignKey(User, related_name="posts")
    slug = models.SlugField(max_length=300, blank=True, default='')

    class Meta:
        ordering = ["date", "title"]

    def get_tags(self):
        return self.tags.all()

    def get_absolute_url(self):
        return reverse('post_list')

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

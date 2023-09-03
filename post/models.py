from django.db import models
from django.utils.text import slugify
# from markdownx.models import MarkdownxField
from markdownx.utils import markdownify
class Post(models.Model):
    post_id = models.AutoField(auto_created=True,primary_key=True)
    author = models.CharField(max_length=30,null=False)
    title = models.CharField(max_length=200)
    intro = models.TextField()
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(null=True, blank=True,unique=True,db_index=True, editable=False)

 

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwarqs ):
        self.slug = slugify(self.title)
        return super().save(*args, **kwarqs)
    
    def formated_markdown(self):
        return markdownify(self.body)
    
    def formated_markdown_intro(self):
        return markdownify(self.intro)
    


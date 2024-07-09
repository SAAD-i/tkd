from django.db import models
from django.conf import settings
# Create your models here.

class ToolCategory(models.Model):
    name = models.CharField(max_length=250, unique=True)
    desc = models.TextField(blank=True)

class Tool(models.Model):
    name = models.CharField(max_length=250,unique=True)
    category = models.ForeignKey(ToolCategory, on_delete=models.SET_DEFAULT, default='Others')
    slug = models.SlugField(max_length=250, unique=True, blank=True)
    is_enabled = models.BooleanField(default=True)
    free_limit = models.IntegerField(default=10)
    free_mb_limit = models.IntegerField(default=100)
    pro_limit = models.IntegerField()
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Tool, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
    
class ToolUsage(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True)
    tool = models.OneToOneField(Tool, on_delete=models.CASCADE)
    usage_date = models.DateTimeField(auto_now_add=True)
    
    
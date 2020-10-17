from django.db import models
from ckeditor.fields import RichTextField
from users.models import UserModel



# Create your models here.

    


# Post Model
class Post(models.Model):
    post_name = models.CharField(max_length=100, default='')
    overview = RichTextField()
    text = RichTextField()
    date_added = models.DateField(auto_now=True)
    author = models.ForeignKey(UserModel(is_admin=True), on_delete = models.CASCADE,null=False)
    likes = models.IntegerField(default=0)
    
    def __str__(self):
        """
        docstring
        """
        return self.post_name



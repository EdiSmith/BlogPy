from django.contrib.auth import get_user_model
from ckeditor.fields import RichTextField
from django.utils import timezone
from django.db import models


def validate_file_ext(value):
    from django.core.exceptions import ValidationError
    import os
    ext = os.path.splitext(value.name)
    valid_format = ['.png','.jpeg']
    if not ext.lower() in valid_format:
        raise ValidationError('Unsupported file extension.')

class UserProfile(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    avatar = models.FileField(upload_to='user_avatar/', null=False, blank=False, validators=[validate_file_ext])
    bio = models.TextField(max_length=250 , null=False, blank=False)

    def __str__(self):
        return self.user.first_name


class Article(models.Model):
    title = models.CharField(max_length=128, null=False, blank=False)
    cover = models.FileField(upload_to='article_cover/', null=False, blank=False, validators=[validate_file_ext])
    body = RichTextField()
    created_at = models.DateTimeField(default=timezone.now, )
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    promote = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=128, null=False, blank=False)
    cover = models.FileField(upload_to='category_cover/', null=False, blank=False, validators=[validate_file_ext])
    
    def __str__(self):
        return self.title

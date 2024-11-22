from django.db import models
from django.core.validators import FileExtensionValidator
# Create your models here.
from django.contrib.auth.models import User
# Create your models here.

class Folder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='folders')
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'folder:{self.name}\t created_at:{self.created_at}\t last_updated:{self.updated_at}'

class File(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='files')
    name = models.CharField(max_length=100)
    folder = models.ForeignKey(Folder, on_delete=models.PROTECT, related_name='files')
    image = models.ImageField(upload_to='media/',null=True,blank=True)
    video = models.FileField(upload_to='media/',
                             validators=[FileExtensionValidator(allowed_extensions=['mov','mp4','mkv'])],
                             null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'user:{self.user}\t upload image:{self.image}\t video:{self.video}\t created_at:{self.created_at}'




from django.db import models

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=200)

    def __str__(self):
        return self.name
    

class FileUpload(models.Model):
    name = models.CharField(max_length=200, default="test")
    text_number = models.CharField(max_length=200, null=True)
    release_date = models.DateField(null=True)
    expiration_date = models.DateField(null=True)
    description = models.TextField(null=True)
    internal_notes = models.CharField(max_length=300, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    active = models.BooleanField(default=True)
    type = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    file = models.FileField(upload_to="fileStore")

    def __str__(self):
        return self.name

    def delete(self, using=None, keep_parents=False):
        self.file.delete()
        super().delete()
    
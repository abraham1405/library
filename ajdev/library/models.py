from django.db import models

class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, verbose_name='Title')
    image = models.ImageField(upload_to='images/', verbose_name='Image', null=True)
    description = models.TextField(verbose_name='Description', null=True)
    
    def __str__(self):
        return f"Title: {self.title} - Description: {self.description or 'No description'}"
    
    def delete(self, using=None, keep_parents=False):
        self.image.storage.delete(self.image.name)
        
        return super().delete(using, keep_parents)
    

